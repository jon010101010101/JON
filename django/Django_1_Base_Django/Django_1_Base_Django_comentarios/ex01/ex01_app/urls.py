# Importa la función path del módulo django.urls para definir rutas URL
from django.urls import path
# Importa las vistas desde el archivo views del directorio actual
from . import views

# Define la lista de patrones de URL para esta aplicación
urlpatterns = [
    # Ruta para la vista 'django_view'
    # Cuando se accede a '/django/', se ejecutará la función django_view en views.py
    path('django/', views.django_view, name='django'),

    # Ruta para la vista 'display_view'
    # Cuando se accede a '/display/', se ejecutará la función display_view en views.py
    path('display/', views.display_view, name='display'),

    # Ruta para la vista 'templates_view'
    # Cuando se accede a '/templates/', se ejecutará la función templates_view en views.py
    path('templates/', views.templates_view, name='templates'),
]
