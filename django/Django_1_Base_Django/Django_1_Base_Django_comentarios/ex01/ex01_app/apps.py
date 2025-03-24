# Importa la función path del módulo django.urls
from django.urls import path
# Importa todas las vistas del módulo views del directorio actual
from . import views

# Define el espacio de nombres de la aplicación
# Esto ayuda a evitar conflictos de nombres entre diferentes aplicaciones
app_name = 'ex01_app'

# Define la lista de patrones de URL para esta aplicación
urlpatterns = [
    # Ruta para la vista 'django_view'
    # Cuando se accede a '/ex01/django/', Django llamará a la función django_view
    path('django/', views.django_view, name='django'),

    # Ruta para la vista 'display_view'
    # Cuando se accede a '/ex01/display/', Django llamará a la función display_view
    path('display/', views.display_view, name='display'),

    # Ruta para la vista 'templates_view'
    # Cuando se accede a '/ex01/templates/', Django llamará a la función templates_view
    path('templates/', views.templates_view, name='templates'),
]
