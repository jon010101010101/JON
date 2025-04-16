from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType


class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.reputation})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # self.update_permissions()  # ¡ELIMINA ESTA LÍNEA!

    def calculate_reputation(self):
        """Calculates the user's reputation based on the votes their tips have received."""
        reputation = 0
        for tip in self.tips.all():
            reputation += tip.upvoted_by.count() * 5
            reputation -= tip.downvoted_by.count() * 2
        return reputation

    def update_reputation(self):
        """Updates the user's reputation."""
        self.reputation = self.calculate_reputation()
        super().save(update_fields=['reputation'])  # Guarda solo el campo de reputación

    def update_permissions(self):
        """Grants or revokes permissions based on reputation."""
        # Get the ContentType for the Tip model
        tip_content_type = ContentType.objects.get_for_model(Tip)

        # Ensure the permissions exist
        can_downvote, created = Permission.objects.get_or_create(
            codename='can_downvote_tip',
            name='Can downvote any Tip',
            content_type=tip_content_type
        )
        can_delete, created = Permission.objects.get_or_create(
            codename='can_delete_tip',
            name='Can delete any Tip',
            content_type=tip_content_type
        )

        if self.reputation >= 15:
            self.user_permissions.add(can_downvote)
        else:
            self.user_permissions.remove(can_downvote)

        if self.reputation >= 30:
            self.user_permissions.add(can_delete)
        else:
            self.user_permissions.remove(can_delete)

        # self.save()  # ¡ELIMINA ESTA LÍNEA!


class Tip(models.Model):
    content = models.TextField("Tip content")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tips")
    date = models.DateTimeField(auto_now_add=True)
    upvoted_by = models.ManyToManyField(CustomUser, related_name='upvoted_tips', blank=True)
    downvoted_by = models.ManyToManyField(CustomUser, related_name='downvoted_tips', blank=True)

    def upvotes(self):
        return self.upvoted_by.count()

    def downvotes(self):
        return self.downvoted_by.count()

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"

    class Meta:
        permissions = [
            ("can_delete_tip", "Can delete any Tip"),
            ("can_downvote_tip", "Can downvote any Tip"),  # New permission
        ]
