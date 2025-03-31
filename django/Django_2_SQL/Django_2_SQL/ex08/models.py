from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=128, blank=True)
    diameter = models.IntegerField(blank=True, null=True)
    orbital_period = models.IntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    rotation_period = models.IntegerField(blank=True, null=True)
    surface_water = models.FloatField(blank=True, null=True)
    terrain = models.CharField(max_length=128, blank=True)

    class Meta:
        db_table = 'ex08_planets'


class Person(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=32, blank=True)
    hair_color = models.CharField(max_length=32, blank=True)
    height = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE, to_field='name', db_column='homeworld')

    class Meta:
        db_table = 'ex08_people'