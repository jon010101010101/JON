from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser.
    Incluye un campo adicional de reputación y lógica para manejar cambios.
    """
    reputation = models.IntegerField(default=0)  # Campo para la reputación
    reputation_changed = False  # Atributo para rastrear cambios en la reputación

    def save(self, *args, **kwargs):
        """
        Detecta cambios en la reputación antes de guardar.
        """
        if self.pk:  # Si el usuario ya existe
            old_reputation = CustomUser.objects.get(pk=self.pk).reputation
            self.reputation_changed = old_reputation != self.reputation
        else:
            self.reputation_changed = True  # Es un usuario nuevo

        super().save(*args, **kwargs)

    def update_reputation(self, delta_upvotes=0, delta_downvotes=0):
        """
        Actualiza la reputación incrementalmente.
        delta_upvotes y delta_downvotes son los cambios en los votos.
        """
        self.reputation += delta_upvotes * 5 - delta_downvotes * 2
        self.save(update_fields=['reputation'])

    @property
    def can_downvote(self):
        """Determina si el usuario puede hacer downvote."""
        return self.reputation >= 15

    @property
    def can_delete_tips(self):
        """Determina si el usuario puede eliminar Tips."""
        return self.reputation >= 30

    def __str__(self):
        return f"{self.username} ({self.reputation} rep)"


class Tip(models.Model):
    """
    Modelo de Tip que representa un contenido creado por un usuario.
    Incluye lógica para manejar votos y eliminación.
    """
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tips'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoted_tips',
        blank=True
    )
    downvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='downvoted_tips',
        blank=True
    )

    def save(self, *args, **kwargs):
        """
        Asegura que la reputación del autor se actualice al crear un Tip.
        """
        is_new = self.pk is None  # Verifica si el Tip es nuevo
        super().save(*args, **kwargs)
        if is_new:
            self.author.update_reputation()

    def delete(self, *args, **kwargs):
        """
        Recalcula la reputación del autor al eliminar un Tip.
        """
        upvotes_count = self.upvotes.count()
        downvotes_count = self.downvotes.count()

        # Verifica si el autor tiene permiso para eliminar el Tip
        if not self.author.can_delete_tips:
            raise PermissionError("No tienes suficiente reputación para eliminar este tip.")

        super().delete(*args, **kwargs)
        self.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)

    def upvote(self, user):
        """
        Maneja la lógica de agregar un upvote.
        """
        if user == self.author:
            raise PermissionError("No puedes votar tu propio tip.")

        if self.upvotes.filter(id=user.id).exists():
            raise PermissionError("Ya has votado positivamente este tip.")

        if self.downvotes.filter(id=user.id).exists():  # Revertir un downvote previo
            self.downvotes.remove(user)
            self.author.update_reputation(delta_downvotes=-1)

        self.upvotes.add(user)
        self.author.update_reputation(delta_upvotes=1)

    def downvote(self, user):
        """
        Maneja la lógica de agregar un downvote.
        """
        if user == self.author:
            raise PermissionError("No puedes votar tu propio tip.")

        if self.downvotes.filter(id=user.id).exists():
            raise PermissionError("Ya has votado negativamente este tip.")

        if self.upvotes.filter(id=user.id).exists():  # Revertir un upvote previo
            self.upvotes.remove(user)
            self.author.update_reputation(delta_upvotes=-1)

        self.downvotes.add(user)
        self.author.update_reputation(delta_downvotes=1)

    def upvotes_count(self):
        """Devuelve el número total de upvotes."""
        return self.upvotes.count()

    def downvotes_count(self):
        """Devuelve el número total de downvotes."""
        return self.downvotes.count()

    def score(self):
        """
        Devuelve el puntaje total del tip (upvotes - downvotes).
        """
        return self.upvotes_count() - self.downvotes_count()

    class Meta:
        permissions = [
            ("can_delete_tip", "Can delete tip"),
            ("can_downvote_tip", "Can downvote a tip"),
        ]