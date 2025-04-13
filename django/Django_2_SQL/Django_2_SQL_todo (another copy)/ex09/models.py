from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.PositiveIntegerField(null=True) 
    population = models.BigIntegerField(null=True)
    rotation_period = models.PositiveIntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=20, null=True, blank=True)  # Permitir valores nulos
    gender = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)  # Permitir valores nulos
    hair_color = models.CharField(max_length=20, null=True, blank=True)  # Permitir valores nulos
    height = models.IntegerField(null=True)  # Permitir valores nulos
    mass = models.FloatField(null=True)  # Permitir valores nulos
    homeworld = models.ForeignKey('Planets', null=True, on_delete=models.SET_NULL)  # Permitir valores nulos
    created = models.DateTimeField(auto_now_add=True)  # Este campo se establece automáticamente
    updated = models.DateTimeField(auto_now=True)  # Este campo se actualiza automáticamente

    def __str__(self):
        return self.name