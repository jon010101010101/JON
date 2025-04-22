from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

    def update_reputation(self, points):
        """
        Updates the user's reputation and dynamically adjusts permissions.
        """
        self.reputation += points
        self.save()
        self.assign_permissions()  # Update permissions dynamically

    def __str__(self):
        return f"{self.username} ({self.reputation})"

    def can_downvote(self):
        """
        Returns True if the user has sufficient reputation to downvote.
        """
        return self.reputation >= 15

    def can_delete_tip(self):
        """
        Returns True if the user has sufficient reputation to delete tips.
        """
        return self.reputation >= 30

    def save(self, *args, **kwargs):
        """
        Ensure permissions are created when the user is created.
        """
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            self.assign_permissions()

    def assign_permissions(self):
        """
        Assigns custom permissions based on the user's reputation.
        """
        content_type = ContentType.objects.get_for_model(CustomUser)

        # Get or create the permissions
        can_downvote_permission, _ = Permission.objects.get_or_create(
            codename='can_downvote',
            name='Can Downvote Tips',
            content_type=content_type,
        )

        can_delete_tip_permission, _ = Permission.objects.get_or_create(
            codename='can_delete_tip',
            name='Can Delete Tips',
            content_type=content_type,
        )

        # Assign permissions based on reputation
        if self.can_downvote():
            self.user_permissions.add(can_downvote_permission)
        else:
            self.user_permissions.remove(can_downvote_permission)

        if self.can_delete_tip():
            self.user_permissions.add(can_delete_tip_permission)
        else:
            self.user_permissions.remove(can_delete_tip_permission)


class Tip(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    upvotes = models.ManyToManyField(CustomUser, related_name='upvoted_tips', blank=True)
    downvotes = models.ManyToManyField(CustomUser, related_name='downvoted_tips', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def upvote(self, user):
        """
        Registers an upvote and updates the author's reputation.
        """
        if user not in self.upvotes.all():
            self.upvotes.add(user)
            self.author.update_reputation(5)

    def downvote(self, user):
        """
        Registers a downvote and updates the author's reputation.
        """
        if user != self.author and user not in self.downvotes.all():
            if user.can_downvote():
                self.downvotes.add(user)
                self.author.update_reputation(-2)
            else:
                raise PermissionError("You don't have enough reputation to downvote.")

    def delete(self, *args, **kwargs):
        """
        Deletes the tip and adjusts the author's reputation.
        """
        self.author.update_reputation(-(self.upvotes.count() * 5))
        self.author.update_reputation(self.downvotes.count() * 2)
        super().delete(*args, **kwargs)