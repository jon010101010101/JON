from django.db import models
from django.contrib.auth.models import User

class Tip(models.Model):
    content = models.TextField("Tip content")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tips")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
