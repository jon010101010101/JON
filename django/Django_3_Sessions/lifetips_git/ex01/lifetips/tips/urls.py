from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # Página principal
    path('register/', views.register, name='register'),  # Registro
    path('login/', views.login_view, name='login'),      # Login
    path('logout/', views.logout_view, name='logout'),   # Logout
]
