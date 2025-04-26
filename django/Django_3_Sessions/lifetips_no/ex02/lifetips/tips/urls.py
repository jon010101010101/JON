from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # Página principal: muestra tips y formulario si logueado
    path('register/', views.register, name='register'),  # Registro de usuario
    path('login/', views.login_view, name='login'),      # Login de usuario
    path('logout/', views.logout_view, name='logout'),   # Logout de usuario
]
