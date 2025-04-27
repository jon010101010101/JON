from django.apps import AppConfig

class TipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ex06.tips'  # Debe coincidir con INSTALLED_APPS

    def ready(self):
        import tips.signals  # Ajusta la ruta si estás utilizando señales