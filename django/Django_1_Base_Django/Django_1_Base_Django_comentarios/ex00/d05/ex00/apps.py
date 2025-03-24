from django.apps import AppConfig  # Importa la clase base 'AppConfig' para configurar aplicaciones de Django


class Ex00Config(AppConfig):
    # Define la configuración predeterminada para los campos automáticos en los modelos de esta aplicación
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Especifica el nombre de la aplicación. Este nombre debe coincidir con el nombre del directorio de la aplicación.
    name = 'ex00'
