"""
URL configuration for the 'tips' app.

This file routes URLs specific to the 'tips' app to their respective views.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from tips.views import (  # Importamos explícitamente solo las vistas necesarias
    home,
    create_tip,
    tips_list,
    vote_tip,
    delete_tip,
    register,
    upvote_tip,  # Nueva vista
    downvote_tip,  # Nueva vista
    CustomPasswordResetView,
)

urlpatterns = [
    # Página principal de la app (listado o inicio)
    path('', home, name='home'),

    # Funciones relacionadas con los tips
    path('create/', create_tip, name='create_tip'),  # Crear un nuevo tip
    path('list/', tips_list, name='tips_list'),  # Listar todos los tips
    path('<int:tip_id>/vote/<str:vote_type>/', vote_tip, name='vote_tip'),  # Votar por un tip
    path('<int:tip_id>/delete/', delete_tip, name='delete_tip'),  # Eliminar un tip
    path('<int:tip_id>/upvote/', upvote_tip, name='upvote_tip'),  # Nueva ruta para "Upvote"
    path('<int:tip_id>/downvote/', downvote_tip, name='downvote_tip'),  # Nueva ruta para "Downvote"

    # Registro de usuarios
    path("register/", register, name="register"),

    # Funciones de Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),

    # Recuperación de contraseña con vistas personalizadas
    path(
        'password_reset/',
        CustomPasswordResetView.as_view(template_name='registration/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset_done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]