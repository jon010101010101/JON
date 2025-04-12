from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=200, blank=True, null=True)
    diameter = models.IntegerField(blank=True, null=True)
    orbital_period = models.IntegerField(blank=True, null=True)  # Nuevo campo
    population = models.BigIntegerField(blank=True, null=True)  # Nuevo campo
    rotation_period = models.IntegerField(blank=True, null=True)  # Nuevo campo
    surface_water = models.FloatField(blank=True, null=True)  # Nuevo campo
    terrain = models.CharField(max_length=255, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64, null=False)  # Coincide con ex09
    birth_year = models.CharField(max_length=10, null=True, blank=True)  # Coincide con ex09
    gender = models.CharField(max_length=32, blank=True)  # Coincide con ex09
    eye_color = models.CharField(max_length=32, null=True, blank=True)  # Coincide con ex09
    hair_color = models.CharField(max_length=32, null=True, blank=True)  # Coincide con ex09
    height = models.IntegerField(null=True, blank=True)  # Coincide con ex09
    mass = models.FloatField(null=True, blank=True)  # Coincide con ex09
    homeworld = models.ForeignKey(Planets, null=True, on_delete=models.SET_NULL)  # Coincide con ex09
    created = models.DateTimeField(auto_now_add=True, null=True)  # Coincide con ex09
    updated = models.DateTimeField(auto_now=True, null=True)  # Coincide con ex09

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)  # Coincide con ex01
    episode_nb = models.IntegerField(primary_key=True)  # Coincide con ex01
    opening_crawl = models.TextField(null=True, blank=True)  # Coincide con ex01
    director = models.CharField(max_length=32, null=True, blank=True)  # Coincide con ex01
    producer = models.CharField(max_length=128, null=False)  # Coincide con ex01 (no debe ser nullable)
    release_date = models.DateField(null=False)  # Coincide con ex01
    characters = models.ManyToManyField(People, related_name='movies')  # Correcto

    def __str__(self):
        return self.title
