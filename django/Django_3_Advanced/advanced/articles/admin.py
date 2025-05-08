from django.contrib import admin
from .models import Article, UserFavouriteArticle

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'synopsis')
    search_fields = ('title', 'author__username', 'synopsis')

@admin.register(UserFavouriteArticle)
class UserFavouriteArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')
    search_fields = ('user__username', 'article__title')
