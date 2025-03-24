# Importa la función path del módulo django.urls para definir rutas URL
from django.urls import path

# Importa el módulo views de la aplicación actual
from . import views

# Define la lista de patrones de URL para esta aplicación
urlpatterns = [
    # Define la ruta raíz de la aplicación
    # Cuando se accede a esta ruta, Django llamará a la función color_table en views.py
    # El parámetro 'name' permite referenciar esta URL en otras partes del proyecto
    path('', views.color_table, name='color_table'),
]
