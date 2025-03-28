""" Configuración ASGI para el proyecto helloworld_project.

Expone la llamada ASGI como una variable a nivel de módulo llamada application.

Para más información sobre este archivo,
 consulta https://docs.djangoproject.com/es/5.1/howto/deployment/asgi/ """



# Importa el módulo 'os' para interactuar con variables de entorno del sistema operativo.
import os

# Importa la función 'get_asgi_application' desde Django para crear una aplicación ASGI.
from django.core.asgi import get_asgi_application

# Establece la variable de entorno 'DJANGO_SETTINGS_MODULE' con el valor 
# 'helloworld_project.settings'
# si no ha sido configurada previamente. Esto es necesario para que Django sepa dónde encontrar
# los ajustes del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld_project.settings')

# Crea la aplicación ASGI utilizando la función 'get_asgi_application' de Django.
# Esta aplicación es la entrada principal para el servidor ASGI.
application = get_asgi_application()
