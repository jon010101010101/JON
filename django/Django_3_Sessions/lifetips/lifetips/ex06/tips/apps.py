from django.apps import AppConfig

class TipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tips'  # Debe coincidir con INSTALLED_APPS

    def ready(self):
        # Importa el archivo donde definiste la señal
        import tips.signals  # Ajusta la ruta según tu estructura de proyecto