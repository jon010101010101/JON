from django.db import models
from django.contrib.auth.models import User

# Modelo para los artículos
class Article(models.Model):
    title = models.CharField(max_length=200)  # Título del artículo
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor del artículo
    synopsis = models.TextField()  # Sinopsis del artículo
    content = models.TextField()  # Contenido completo del artículo
    created = models.DateTimeField(auto_now_add=True)  # Fecha de creación del artículo

    def __str__(self):
        return self.title

    # Método utilitario para truncar la sinopsis
    def short_synopsis(self, length=100):
        return self.synopsis[:length] + "..." if len(self.synopsis) > length else self.synopsis


# Modelo para los artículos favoritos de los usuarios
class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Artículo favorito

    class Meta:
        unique_together = ("user", "article")  # Asegura que un usuario no pueda añadir el mismo artículo dos veces como favorito

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"