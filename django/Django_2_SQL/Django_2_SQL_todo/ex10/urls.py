from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_characters, name='search_characters'),  # Map the empty path to the view
]
