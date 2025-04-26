from django.apps import AppConfig


class TipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tips'

    def ready(self):
        import tips.signals  # Importa las señales cuando la aplicación esté lista