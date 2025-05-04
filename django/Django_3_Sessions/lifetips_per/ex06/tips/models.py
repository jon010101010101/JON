from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import transaction
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

class CustomUser(AbstractUser):
    """
    Modelo personalizado de usuario que extiende AbstractUser.
    Incluye campos adicionales para gestionar reputación y control de cambio de contraseña.
    """
    reputation = models.IntegerField(default=0, help_text="Reputación del usuario.")
    can_change_password = models.BooleanField(default=True, help_text="¿Puede el usuario cambiar su contraseña?")
    reputation_changed = False  # Atributo no persistente que rastrea cambios en la reputación
    last_password_reset_request = models.DateTimeField(
        null=True, blank=True, help_text="Fecha y hora de la última solicitud de restablecimiento de contraseña."
    )

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para detectar cambios en la reputación del usuario.
        """
        if self.pk:  # Si el usuario ya existe
            old_reputation = CustomUser.objects.get(pk=self.pk).reputation
            self.reputation_changed = old_reputation != self.reputation
        else:
            self.reputation_changed = True  # Es un usuario nuevo

        super().save(*args, **kwargs)

    def update_reputation(self, delta_upvotes=0, delta_downvotes=0):
        """
        Actualiza la reputación del usuario basado en los deltas de votos positivos y negativos.
        """
        new_reputation = self.reputation + delta_upvotes * 5 - delta_downvotes * 2
        self.reputation = max(new_reputation, -20)  # Límite inferior de reputación a -20
        self.save(update_fields=['reputation'])

    @property
    def can_downvote(self):
        """
        Verifica si el usuario puede emitir votos negativos.
        """
        return self.reputation >= 15

    @property
    def can_delete_tips(self):
        """
        Verifica si el usuario puede eliminar tips.
        """
        return self.reputation >= 30

    def __str__(self):
        """
        Devuelve una representación en cadena del usuario.
        """
        return f"{self.username} ({self.reputation} rep)"


class Tip(models.Model):
    """
    Modelo para representar un Tip (consejo) creado por los usuarios.
    Incluye funcionalidad para votos positivos y negativos.
    """

    title = models.CharField(
        max_length=200, verbose_name="Título", default="Título por defecto"
    )
    content = models.TextField(verbose_name="Contenido")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tips',
        verbose_name="Autor",
        help_text="Usuario que creó el tip."
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoted_tips',
        blank=True,
        verbose_name="Votado positivamente por"
    )
    downvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='downvoted_tips',
        blank=True,
        verbose_name="Votado negativamente por"
    )

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para actualizar la reputación del autor
        si se trata de un nuevo Tip.
        """
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.author.update_reputation()

    def delete(self, *args, **kwargs):
        """
        Sobrescribe el método delete para ajustar la reputación del autor
        antes de eliminar el Tip.

        Parámetros:
        - user (CustomUser): Usuario que intenta eliminar el Tip.
        """
        user = kwargs.pop("user", None)
        if user != self.author and not user.is_superuser:
            raise PermissionError("No tienes permiso para eliminar este tip.")

        # Contar los votos antes de eliminar
        upvotes_count = self.upvotes.count()
        downvotes_count = self.downvotes.count()

        # Ajustar la reputación del autor
        self.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)

        # Eliminar el tip
        super().delete(*args, **kwargs)

    def upvote(self, user):
        """
        Permite a un usuario emitir un voto positivo en este tip.
        """
        with transaction.atomic():
            if user == self.author:
                raise PermissionError("No puedes votar positivamente tu propio tip.")
            if self.upvotes.filter(id=user.id).exists():
                raise PermissionError("Ya has votado positivamente este tip.")
            if self.downvotes.filter(id=user.id).exists():
                self.downvotes.remove(user)
                self.author.update_reputation(delta_downvotes=-1)

            self.upvotes.add(user)
            self.author.update_reputation(delta_upvotes=1)

            logger.info(f"Usuario {user} votó positivamente el Tip {self.id}")

    def downvote(self, user):
        """
        Permite a un usuario emitir un voto negativo en este tip.
        """
        with transaction.atomic():
            if user == self.author:
                raise PermissionError("No puedes votar negativamente tu propio tip.")
            if self.downvotes.filter(id=user.id).exists():
                raise PermissionError("Ya has votado negativamente este tip.")
            if self.upvotes.filter(id=user.id).exists():
                self.upvotes.remove(user)
                self.author.update_reputation(delta_upvotes=-1)

            self.downvotes.add(user)
            self.author.update_reputation(delta_downvotes=1)

            logger.info(f"Usuario {user} votó negativamente el Tip {self.id}")

    def upvotes_count(self):
        """
        Devuelve el número de votos positivos.
        """
        return self.upvotes.count()

    def downvotes_count(self):
        """
        Devuelve el número de votos negativos.
        """
        return self.downvotes.count()

    def score(self):
        """
        Calcula el puntaje neto del tip (votos positivos - votos negativos).
        """
        return self.upvotes_count() - self.downvotes_count()

    class Meta:
        permissions = [
            ("can_delete_tip", "Puede eliminar un tip"),
            ("can_downvote_tip", "Puede votar negativamente un tip"),
        ]
