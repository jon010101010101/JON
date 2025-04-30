"""
URL configuration for ex06 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
=======
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404  # Importa handler404
from tips import views as tips_views  # Agrega las vistas principales aquí
>>>>>>> aa7cf094 (Remove unused files and clean up project)

# Configuración del manejador de errores 404
handler404 = 'tips.views.custom_404_view'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tip, name='create_tip'),
    path('<int:tip_id>/vote/<str:vote_type>/', views.vote_tip, name='vote_tip'),
    path('<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
