"""
Configuración de ASGI para el proyecto color_table.

Expone el objeto invocable ASGI como una variable a nivel de módulo llamada `application`.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


# Importa el módulo 'os' para interactuar con el sistema operativo
import os

# Importa la función 'get_asgi_application' del módulo 'django.core.asgi'
from django.core.asgi import get_asgi_application

# Configura la variable de entorno 'DJANGO_SETTINGS_MODULE'
# Esto le indica a Django dónde encontrar el archivo de configuración principal
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'color_table.settings')

# Crea una instancia de la aplicación ASGI de Django
# Esta será la interfaz entre el servidor web y tu aplicación Django
application = get_asgi_application()
