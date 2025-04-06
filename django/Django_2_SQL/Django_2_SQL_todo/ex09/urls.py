from django.urls import path
from .views import display_characters

urlpatterns = [
    path('display/', display_characters, name='display_characters'),
]