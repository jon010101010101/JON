from django.db import models

class MyModel(models.Model):
    # Define los campos de tu modelo aquí
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
