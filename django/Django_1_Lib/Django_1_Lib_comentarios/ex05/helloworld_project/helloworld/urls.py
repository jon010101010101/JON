# Importa el módulo path de django.urls para definir rutas URL
from django.urls import path
# Importa las vistas de la aplicación actual
from . import views

# Define una lista de rutas URL para esta aplicación
urlpatterns = [
    # Define la ruta raíz para esta aplicación, asociada a la vista hello_world
    path('', views.hello_world, name='hello_world'),  
]
