from django.urls import path
from .views import Init, Populate, Display  # Asegúrate de que estás importando las clases correctamente

urlpatterns = [
    path('init/', Init.as_view(), name='init'),  # Ruta para crear las tablas
    path('populate/', Populate.as_view(), name='populate'),  # Ruta para poblar las tablas
    path('display/', Display.as_view(), name='display'),  # Ruta para mostrar los datos
]