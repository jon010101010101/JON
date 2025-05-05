from django.urls import path
from . import views  # <--- IMPORTANTE: from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
