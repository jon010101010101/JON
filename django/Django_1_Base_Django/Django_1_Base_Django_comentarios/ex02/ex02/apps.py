from django.apps import AppConfig


class Ex02Config(AppConfig):
    # Define el tipo de campo automático predeterminado para los modelos de esta aplicación
    # En este caso, se usa BigAutoField para soportar un mayor rango de valores
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Especifica el nombre de la aplicación
    # Este nombre debe coincidir con el nombre del directorio de la aplicación
    name = 'ex02'
