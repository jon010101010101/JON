from django.urls import path
from .views import ex00

urlpatterns = [
    path('init/', views.init, name='ex00-init'),
]
