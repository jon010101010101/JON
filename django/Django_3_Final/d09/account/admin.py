from django.contrib import admin
from .models import Article, UserFavouriteArticle

# Configuración del modelo Article en el administrador
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created')  # Campos visibles en la lista
    search_fields = ('title', 'author__username')  # Campos por los que se puede buscar
    list_filter = ('author', 'created')  # Filtros laterales


# Configuración del modelo UserFavouriteArticle en el administrador
@admin.register(UserFavouriteArticle)
class UserFavouriteArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article')  # Campos visibles en la lista
    search_fields = ('user__username', 'article__title')  # Campos por los que se puede buscar
    list_filter = ('user', 'article')  # Filtros laterales