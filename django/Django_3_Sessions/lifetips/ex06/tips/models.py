from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import transaction
import logging

logger = logging.getLogger(__name__)


class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)  # Campo para la reputación
    reputation_changed = False  # Atributo para rastrear cambios en la reputación

    def save(self, *args, **kwargs):
        if self.pk:  # Si el usuario ya existe
            old_reputation = CustomUser.objects.get(pk=self.pk).reputation
            self.reputation_changed = old_reputation != self.reputation
        else:
            self.reputation_changed = True  # Es un usuario nuevo

        super().save(*args, **kwargs)

    def update_reputation(self, delta_upvotes=0, delta_downvotes=0):
        new_reputation = self.reputation + delta_upvotes * 5 - delta_downvotes * 2
        self.reputation = max(new_reputation, -20)  # Límite inferior de reputación
        self.save(update_fields=['reputation'])

    @property
    def can_downvote(self):
        return self.reputation >= 15

    @property
    def can_delete_tips(self):
        return self.reputation >= 30

    def __str__(self):
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
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.author.update_reputation()

    def delete(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        if user != self.author and not user.is_superuser:
            raise PermissionError("You don't have permission to delete this tip.")

        upvotes_count = self.upvotes.count()
        downvotes_count = self.downvotes.count()

        super().delete(*args, **kwargs)
        self.author.update_reputation(delta_upvotes=-upvotes_count, delta_downvotes=-downvotes_count)

    def upvote(self, user):
        with transaction.atomic():
            if user == self.author:
                raise PermissionError("You cannot upvote your own tip.")
            if self.upvotes.filter(id=user.id).exists():
                raise PermissionError("You have already upvoted this tip.")
            if self.downvotes.filter(id=user.id).exists():
                self.downvotes.remove(user)
                self.author.update_reputation(delta_downvotes=-1)

            self.upvotes.add(user)
            self.author.update_reputation(delta_upvotes=1)

            logger.info(f"User {user} upvoted Tip {self.id}")

    def downvote(self, user):
        with transaction.atomic():
            if user == self.author:
                raise PermissionError("You cannot downvote your own tip.")
            if self.downvotes.filter(id=user.id).exists():
                raise PermissionError("You have already downvoted this tip.")
            if self.upvotes.filter(id=user.id).exists():
                self.upvotes.remove(user)
                self.author.update_reputation(delta_upvotes=-1)

            self.downvotes.add(user)
            self.author.update_reputation(delta_downvotes=1)

            logger.info(f"User {user} downvoted Tip {self.id}")

    def upvotes_count(self):
        return self.upvotes.count()

    def downvotes_count(self):
        return self.downvotes.count()

    def score(self):
        return self.upvotes_count() - self.downvotes_count()

    class Meta:
        permissions = [
            ("can_delete_tip", "Can delete tip"),
            ("can_downvote_tip", "Can downvote a tip"),
        ]