"""
Configuración de URLs para el proyecto color_table.

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

# Importa las funciones path e include del módulo django.urls
from django.urls import path, include
# Importa el módulo admin de Django para la interfaz de administración
from django.contrib import admin

# Define la lista de patrones de URL para el proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    # Cuando se accede a '/admin/', Django utilizará las URLs predefinidas del admin
    path('admin/', admin.site.urls),
    
    # Ruta para la aplicación table_app
    # Cuando se accede a '/ex03/', Django incluirá las URLs definidas en table_app.urls
    # Esto permite organizar las URLs de la aplicación table_app en su propio archivo
    path('ex03/', include('table_app.urls')),  # Define la URL /ex03
]
