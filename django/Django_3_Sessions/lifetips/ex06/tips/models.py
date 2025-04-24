from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Customized user model with a reputation field.
    """
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.reputation})"

    def save(self, *args, **kwargs):
        # Detect if the user is new
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            self.assign_permissions()

    def assign_permissions(self):
        """Assigns permissions based on reputation."""
        # Get content type for CustomUser
        content_type = ContentType.objects.get_for_model(CustomUser)

        # Get or create permissions
        can_downvote_permission, created = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            defaults={
                'name': 'Can downvote tip',
                'content_type': content_type,
            }
        )
        can_delete_tip_permission, created = Permission.objects.get_or_create(
            codename='can_delete_tip',
            defaults={
                'name': 'Can delete tip',
                'content_type': content_type,
            }
        )

        # Assign downvote permission
        if self.reputation >= 15 and not self.user_permissions.filter(codename='can_downvote_tip').exists():
            self.user_permissions.add(can_downvote_permission)
        elif self.reputation < 15:
            self.user_permissions.remove(can_downvote_permission)

        # Assign delete tip permission
        if self.reputation >= 30 and not self.user_permissions.filter(codename='can_delete_tip').exists():
            self.user_permissions.add(can_delete_tip_permission)
        elif self.reputation < 30:
            self.user_permissions.remove(can_delete_tip_permission)

    def update_reputation(self, points):
        """Updates reputation and assigns permissions."""
        self.reputation += points
        self.save(update_fields=["reputation"])  # Optimize save to only update the reputation field
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

    def add_upvote(self, user):
        """Adds an upvote for the tip if the user hasn't already upvoted or downvoted."""
        if user == self.author:
            return False  # No puedes votar por tu propio tip
        if self.downvotes.filter(id=user.id).exists():
            self.downvotes.remove(user)
            self.author.update_reputation(2)  # Revertir efecto del downvote
        if not self.upvotes.filter(id=user.id).exists():
            self.upvotes.add(user)
            self.author.update_reputation(5)
            return True
        return False  # Voto duplicado

    def add_downvote(self, user):
        """Adds a downvote for the tip if the user hasn't already downvoted or upvoted."""
        if user == self.author:
            return False  # No puedes votar por tu propio tip
        if user.reputation < 15 and not user.is_superuser:
            return False  # No tiene suficiente reputación
        if self.upvotes.filter(id=user.id).exists():
            self.upvotes.remove(user)
            self.author.update_reputation(-5)  # Revertir efecto del upvote
        if not self.downvotes.filter(id=user.id).exists():
            self.downvotes.add(user)
            self.author.update_reputation(-2)
            return True
        return False  # Voto duplicado

    def remove_vote(self, user):
        """Removes a user's vote, either upvote or downvote."""
        if self.upvotes.filter(id=user.id).exists():
            self.upvotes.remove(user)
            self.author.update_reputation(-5)
        elif self.downvotes.filter(id=user.id).exists():
            self.downvotes.remove(user)
            self.author.update_reputation(2)

    def can_delete(self, user):
        """Checks if the user can delete the tip."""
        return user.is_superuser or user.reputation >= 30

    def delete(self, *args, **kwargs):
        """Deletes the tip and clears all associated votes."""
        if not kwargs.pop('force_delete', False) and not self.can_delete(self.author):
            raise PermissionError("User does not have permission to delete this tip.")
        for user in self.upvotes.all():
            self.remove_vote(user)
        for user in self.downvotes.all():
            self.remove_vote(user)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Tip by {self.author.username} - {self.content[:30]}"