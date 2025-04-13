from django.db import models

class Movie(models.Model):
    episode_nb = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    opening_crawl = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    updated = models.DateTimeField(auto_now=True)  # Fecha de actualización automática

    def __str__(self):
        return self.title
