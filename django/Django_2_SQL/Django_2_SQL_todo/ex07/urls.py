from django.urls import path
from . import views

app_name = 'ex07'  # Esto es importante para el namespacing

urlpatterns = [
    path('display/', views.display, name='display'),
    path('update/', views.update, name='update'),
    path('populate/', views.populate, name='populate'),
]
