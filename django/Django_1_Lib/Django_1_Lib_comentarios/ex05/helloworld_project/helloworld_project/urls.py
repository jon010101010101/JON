"""
Vistas basadas en funciones
1. Añade una importación: from mi_app import views
2. Agrega una URL a urlpatterns: path('', views.inicio, name='inicio')

Vistas basadas en clases
1. Añade una importación: from otra_app.views import Inicio
2. Agrega una URL a urlpatterns: path('', Inicio.as_view(), name='inicio')

Incluyendo otra configuración de URLs (URLconf)
1. Importa la función include(): from django.urls import include, path
2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Incluye las URLs de la aplicación 'helloworld'
    path('', include('helloworld.urls')),  
]
