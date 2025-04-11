from django.urls import path
from . import views

urlpatterns = [
    # Esta línea define una ruta URL para la vista 'init'
    # Cuando se accede a '/init/', se ejecuta la función 'init' definida en el módulo 'views'
    # 'name='init'' asigna un nombre a esta ruta, que puede ser utilizado para referenciarla en otras partes del código
    path('init/', views.init, name='init'),
]
