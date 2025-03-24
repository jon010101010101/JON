"""
Configuración WSGI para el proyecto d05.

Expone el objeto invocable WSGI como una variable a nivel de módulo llamada ``application``.

Para obtener más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""


import os  # Importa el módulo 'os' para interactuar con el sistema operativo

from django.core.wsgi import get_wsgi_application  # Importa la función para obtener la aplicación WSGI de Django

# Configura la variable de entorno que Django usa para localizar el archivo de configuración
# Si no está configurada, la establece como 'd05.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd05.settings')

# Crea una instancia de la aplicación WSGI
# Esta es la interfaz entre el servidor web y tu aplicación Django
application = get_wsgi_application()
