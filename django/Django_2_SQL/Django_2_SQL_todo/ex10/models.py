from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.IntegerField(null=True)
    climate = models.CharField(max_length=100, null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.IntegerField(null=True)
    terrain = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=32, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    hair_color = models.CharField(max_length=20, null=True, blank=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=True)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    characters = models.ManyToManyField(People, related_name='movies')  

    def __str__(self):
        return self.title
