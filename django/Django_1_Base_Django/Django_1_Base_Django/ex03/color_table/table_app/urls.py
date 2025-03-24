from django.urls import path
from . import views

urlpatterns = [
    path('', views.color_table, name='color_table'),
]
