from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name='home'),  # Agregar esta línea para la raíz
    path('init/', views.init, name='init'),
]