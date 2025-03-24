from django.urls import path  # Importa la función path de Django para definir rutas URL
from . import views  # Importa el módulo de vistas de la aplicación actual

urlpatterns = [
    # Define la ruta URL para la vista markdown_cheatsheet
    # '' indica que esta es la ruta raíz de la aplicación
    # views.markdown_cheatsheet es la función de vista que manejará las solicitudes a esta ruta
    # name='markdown_cheatsheet' asigna un nombre a esta ruta para referenciarla en otras partes del proyecto
    path('', views.markdown_cheatsheet, name='markdown_cheatsheet'),
]
