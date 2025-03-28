from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init_view, name='init'),  # Ruta para /ex00/init.
]
