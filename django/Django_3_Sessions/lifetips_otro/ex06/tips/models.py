from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.conf import settings
from django.db.models import F
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    """
    Customized user model with a reputation field.
    """
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.reputation})"

    def assign_permissions(self):
        """Asignar permisos según la reputación."""
        content_type = ContentType.objects.get_for_model(CustomUser)
        can_downvote_permission, created = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            content_type=content_type,
            defaults={'name': 'Can downvote tip'}
        )
        can_delete_permission, created = Permission.objects.get_or_create(
            codename='can_delete_tip',
            content_type=content_type,
            defaults={'name': 'Can delete tip'}
        )

        if self.reputation >= 10:
            self.user_permissions.add(can_downvote_permission)
        else:
            self.user_permissions.remove(can_downvote_permission)

        if self.reputation >= 30:
            self.user_permissions.add(can_delete_permission)
        else:
            self.user_permissions.remove(can_delete_permission)

    def update_reputation(self, increment):
        """Actualizar la reputación del usuario y manejar permisos."""
        self.reputation = F('reputation') + increment
        self.save()
        self.refresh_from_db()
        self.assign_permissions()


class Tip(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tips'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
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

    class Meta:
        permissions = [
            ("can_downvote_tip", "Can downvote a tip"),
            ("can_delete_tip", "Can delete a tip"),
        ]

    def add_upvote(self, user):
        """Agregar un upvote al tip."""
        if not self.pk:
            raise ValueError("Cannot vote on a deleted tip.")
        if user == self.author:
            return False
        if self.upvotes.filter(id=user.id).exists():
            return False
        if self.downvotes.filter(id=user.id).exists():
            self.downvotes.remove(user)
            self.author.update_reputation(2)
        self.upvotes.add(user)
        self.author.update_reputation(5)
        return True

    def add_downvote(self, user):
        """Agregar un downvote al tip."""
        if not self.pk:
            raise ValueError("Cannot vote on a deleted tip.")
        if not user.has_perm('tips.can_downvote_tip') and not user.is_superuser:
            return False
        if user == self.author:
            return False
        if self.downvotes.filter(id=user.id).exists():
            return False
        if self.upvotes.filter(id=user.id).exists():
            self.upvotes.remove(user)
            self.author.update_reputation(-5)
        self.downvotes.add(user)
        self.author.update_reputation(-2)
        return True

    def delete(self, *args, **kwargs):
        """Eliminar el tip y revertir el impacto de los votos."""
        # for user in self.upvotes.all(): # Eliminar esta linea
        #     self.upvotes.remove(user)
        # self.author.update_reputation(-5) # Eliminar esta linea
        # for user in self.downvotes.all(): # Eliminar esta linea
        #     self.downvotes.remove(user)
        # self.author.update_reputation(2) # Eliminar esta linea
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Tip by {self.author.username} - {self.content[:30]}"
