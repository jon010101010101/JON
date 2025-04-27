from django.apps import AppConfig

class TipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tips'  # Asegúrate de que coincide con INSTALLED_APPS
    label = 'tips'  # Define el app_label explícitamente como 'tips'

    def ready(self):
        import tips.signals  # Ajusta la ruta si estás utilizando señales