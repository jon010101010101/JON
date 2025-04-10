from django.urls import path
from .views import search_characters

urlpatterns = [
    path('', search_characters, name='search_characters'),  # Ruta raíz para ex10
]
