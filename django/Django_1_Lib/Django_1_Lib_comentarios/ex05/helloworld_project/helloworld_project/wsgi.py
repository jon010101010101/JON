""" Configuración WSGI para el proyecto helloworld_project.

Expone la llamada WSGI como una variable a nivel de módulo llamada application.

Para más información sobre este archivo, 
consulta https://docs.djangoproject.com/es/5.1/howto/deployment/wsgi/ """

import os

from django.core.wsgi import get_wsgi_application

# Establece el valor predeterminado para la variable de entorno 'DJANGO_SETTINGS_MODULE'
# que indica el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld_project.settings')

# Obtiene la aplicación WSGI para el proyecto
application = get_wsgi_application()
