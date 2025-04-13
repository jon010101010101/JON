from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search'),  # Ruta para la vista de búsqueda
]
