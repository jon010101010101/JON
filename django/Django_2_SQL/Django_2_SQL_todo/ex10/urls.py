from django.urls import path
from .views import search_characters

urlpatterns = [
    path('search/', search_characters, name='search_characters'),
]