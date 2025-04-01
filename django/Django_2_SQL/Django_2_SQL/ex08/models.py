from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=255)
    # Otros campos del modelo

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    # Otros campos del modelo

    def __str__(self):
        return self.name
