"""
Configuración de WSGI para el proyecto color_table.

Expone el objeto invocable WSGI como una variable a nivel de módulo llamada `application`.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Importa el módulo 'os' para interactuar con el sistema operativo
import os

# Importa la función 'get_wsgi_application' del módulo 'django.core.wsgi'
from django.core.wsgi import get_wsgi_application

# Configura la variable de entorno 'DJANGO_SETTINGS_MODULE'
# Esto le indica a Django dónde encontrar el archivo de configuración principal
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'color_table.settings')

# Crea una instancia de la aplicación WSGI de Django
# Esta será la interfaz entre el servidor web y tu aplicación Django
application = get_wsgi_application()
