"""
Configuración de URLs para el proyecto config.

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

# Importa la función path del módulo urls de Django para definir rutas
from django.urls import path

# Importa la vista ex02_view desde el archivo views.py de la aplicación ex02
from ex02.views import ex02_view

# Define la lista de patrones de URL para el proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    # Cuando se accede a '/admin/', Django utilizará las URLs predefinidas del admin
    path('admin/', admin.site.urls),
    
    # Ruta para la vista ex02_view
    # Cuando se accede a '/ex02/', Django llamará a la función ex02_view
    # El parámetro 'name' permite referenciar esta URL en otras partes del proyecto
    path('ex02/', ex02_view, name='ex02'),
]
