from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.username

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
            ("can_downvote_tip", "Can downvote any Tip"),  # Nuevo permiso
        ]
