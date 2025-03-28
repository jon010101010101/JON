# Importamos la clase AppConfig desde django.apps para definir la configuración de nuestra aplicación.
from django.apps import AppConfig

# Definimos una clase llamada HelloworldConfig que hereda de AppConfig.
class HelloworldConfig(AppConfig):
    # Establecemos el campo automático por defecto para los modelos de Django.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Especificamos el nombre de la aplicación.
    name = 'helloworld'
