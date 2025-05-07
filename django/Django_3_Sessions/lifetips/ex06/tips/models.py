from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import transaction
from django.utils.timezone import now
from django.core.exceptions import PermissionDenied
import logging

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)  # Campo para la reputación
    reputation_changed = False  # Atributo para rastrear cambios en la reputación
    last_password_reset_request = models.DateTimeField(null=True, blank=True)  # Nuevo campo para rastrear solicitudes de restablecimiento

    def save(self, *args, **kwargs):
        """
        Guarda el usuario y detecta si su reputación ha cambiado.
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
        El superusuario siempre puede.
        """
        return self.is_superuser or self.reputation >= 15

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
    title = models.CharField(max_length=200, verbose_name="Title", default="Default Title")
    content = models.TextField(verbose_name="Content")  # Campo para el contenido del tip
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tips',
        verbose_name="Author"
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='upvoted_tips',
        blank=True,
        verbose_name="Upvoted By"
    )
    downvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='downvoted_tips',
        blank=True,
        verbose_name="Downvoted By"
    )

    def save(self, *args, **kwargs):
        """
        Guarda la instancia de Tip y actualiza la reputación del autor si es un nuevo tip.
        """
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.author.update_reputation()

    def delete(self, *args, **kwargs):
        """
        Elimina la instancia del Tip y ajusta la reputación del autor en función de los votos recibidos.

        - Resta la reputación obtenida por los votos positivos y negativos de este tip.
        - Luego elimina el tip de la base de datos.
        """
        # Contar los votos antes de eliminar
        upvotes_count = self.upvotes.count()
        downvotes_count = self.downvotes.count()

        # Ajustar la reputación del autor restando la influencia de los votos de este tip
        self.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)

        # Llamar al método delete original para eliminar el tip
        super().delete(*args, **kwargs)

    def upvote(self, user):
        """
        Permite a un usuario emitir un voto positivo (upvote) en este tip.

        - Un usuario no puede votar a favor de su propio tip.
        - Un usuario no puede votar a favor el mismo tip más de una vez.
        - Si el usuario había votado en contra previamente, se elimina ese downvote y se ajusta la reputación.
        - Solo se permite un voto por usuario por tip.
        """
        with transaction.atomic():
            # Verifica que el usuario no sea el autor del tip
            if user == self.author:
                raise PermissionDenied("You cannot upvote your own tip.")

            # Verifica que el usuario no haya votado a favor previamente
            if self.upvotes.filter(id=user.id).exists():
                raise PermissionDenied("You have already upvoted this tip.")

            # Si el usuario tenía un voto en contra, lo elimina y ajusta la reputación
            if self.downvotes.filter(id=user.id).exists():
                self.downvotes.remove(user)
                self.author.update_reputation(delta_downvotes=-1)

            # Añade el voto a favor y actualiza la reputación
            self.upvotes.add(user)
            self.author.update_reputation(delta_upvotes=1)

            # Registra la acción en el log
            logger.info(f"User {user} upvoted Tip {self.id}")




    def downvote(self, user):
        """
        Permite a un usuario emitir un voto negativo en este tip.
        El usuario solo puede votar en contra si tiene al menos 15 puntos de reputación,
        excepto si es superusuario.
        Si ya había votado a favor, se elimina ese voto.
        Solo se permite un voto por usuario por tip.
        """
        with transaction.atomic():
            if user == self.author:
                raise PermissionDenied("You cannot downvote your own tip.")
            # Permitir al superusuario downvotar siempre
            if not user.can_downvote and not user.is_superuser:
                raise PermissionDenied("You need at least 15 reputation points to downvote tips.")
            if self.downvotes.filter(id=user.id).exists():
                raise PermissionDenied("You have already downvoted this tip.")
            if self.upvotes.filter(id=user.id).exists():
                # Si tenía un upvote, lo quitamos y ajustamos reputación
                self.upvotes.remove(user)
                self.author.update_reputation(delta_upvotes=-1)
            self.downvotes.add(user)
            self.author.update_reputation(delta_downvotes=1)
            logger.info(f"User {user} downvoted Tip {self.id}")

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
            ("can_delete_tip", "Can delete tip"),
            ("can_downvote_tip", "Can downvote a tip"),
        ]