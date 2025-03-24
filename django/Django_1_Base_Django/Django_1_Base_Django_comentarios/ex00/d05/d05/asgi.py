"""
Configuración ASGI para el proyecto d05.

Expone el objeto invocable ASGI como una variable a nivel de módulo llamada ``application``.

Para obtener más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


import os  # Importa el módulo 'os' para interactuar con las variables de entorno
# del sistema operativo

from django.core.asgi import get_asgi_application  # Importa la función 
# 'get_asgi_application' de Django para configurar la aplicación ASGI

# Establece la variable de entorno 'DJANGO_SETTINGS_MODULE' con el nombre del 
# archivo de configuración del proyecto ('d05.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd05.settings')

# Obtiene la aplicación ASGI configurada para el proyecto. Esta es la instancia 
# que manejará las solicitudes ASGI.
application = get_asgi_application()

