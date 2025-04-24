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
        """Handles the addition of an upvote."""
        if user in self.downvotes.all():
            self.downvotes.remove(user)
            self.author.update_reputation(2)  # Recover reputation lost by downvote
        if user not in self.upvotes.all():
            self.upvotes.add(user)
            self.author.update_reputation(5)

    def add_downvote(self, user):
        """Handles the addition of a downvote."""
        if user.reputation < 2:
            return False  # Do not allow downvote if reputation is less than 2
        if user in self.upvotes.all():
            self.upvotes.remove(user)
            self.author.update_reputation(-5)  # Remove reputation gained from upvote
        if user not in self.downvotes.all():
            self.downvotes.add(user)
            self.author.update_reputation(-2)
        return True

    def remove_upvote(self, user):
        """Handles the removal of an upvote."""
        if user in self.upvotes.all():
            self.upvotes.remove(user)
            self.author.update_reputation(-5)

    def remove_downvote(self, user):
        """Handles the removal of a downvote."""
        if user in self.downvotes.all():
            self.downvotes.remove(user)
            self.author.update_reputation(2)

    def __str__(self):
        return f"Tip by {self.author.username} - {self.content[:30]}"