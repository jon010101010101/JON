from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)  # Título único, no nulo, máx. 64 caracteres
    episode_nb = models.IntegerField(primary_key=True)  # Número del episodio como clave primaria
    opening_crawl = models.TextField(null=True, blank=True)  # Texto opcional (puede ser nulo)
    director = models.CharField(max_length=32, null=False)  # Director no nulo, máx. 32 caracteres
    producer = models.CharField(max_length=128, null=False)  # Productor no nulo, máx. 128 caracteres
    release_date = models.DateField(null=False)  # Fecha de lanzamiento no nula

    def __str__(self):
        return self.title  # Devuelve el título como representación del objeto
