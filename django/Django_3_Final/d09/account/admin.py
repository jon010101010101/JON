from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created')
    search_fields = ('title', 'author__username')
    list_filter = ('author', 'created')
