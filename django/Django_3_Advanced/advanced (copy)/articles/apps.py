from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        # Fuerza la importación de los filtros personalizados
        import articles.templatetags.article_filters
