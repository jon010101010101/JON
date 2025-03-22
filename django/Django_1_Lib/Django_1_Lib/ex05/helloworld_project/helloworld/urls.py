from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),  # Defines the root route for this application
]

