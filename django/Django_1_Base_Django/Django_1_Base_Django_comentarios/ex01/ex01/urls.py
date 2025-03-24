"""
Configuración de URLs para el proyecto ex01.

La lista `urlpatterns` enruta las URLs a las vistas. Para obtener más información, consulta:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Agrega una importación:  from mi_app import views
    2. Agrega una URL a urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación:  from otra_app.views import Home
    2. Agrega una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importa el módulo admin de Django para gestionar la interfaz de administración
from django.contrib import admin

# Importa las funciones path y include del módulo urls de Django
from django.urls import path, include

# Define la lista de patrones de URL para el proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    # Cuando se accede a '/admin/', Django utilizará las URLs predefinidas del admin
    path('admin/', admin.site.urls),
    
    # Ruta para la aplicación 'ex01_app'
    # Incluye todas las URLs definidas en el archivo urls.py de 'ex01_app'
    # Todas estas URLs tendrán el prefijo 'ex01/'
    path('ex01/', include('ex01_app.urls')),
]

