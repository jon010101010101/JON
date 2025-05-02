from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from tips.views import delete_tip
from tips.views import (  
    home,
    create_tip,
    tips_list,
    upvote_tip,
    downvote_tip,
    delete_tip,
    register,
    CustomPasswordResetView,
    users_list  # Importamos la vista users_list
)

# Vista para probar la página 404
def test_404_view(request):
    return render(request, '404.html', status=404)

urlpatterns = [
    # Página principal de la app (listado o inicio)
    path('', home, name='tips_home'),  # Cambié el nombre a 'tips_home' para evitar conflictos con la raíz

    # Funciones relacionadas con los tips
    path('create/', create_tip, name='create_tip'),  # Crear un nuevo tip
    path('list/', tips_list, name='tips_list'),  # Listar todos los tips
    path('<int:tip_id>/delete/', delete_tip, name='delete_tip'),  # Eliminar un tip
    path('<int:tip_id>/upvote/', upvote_tip, name='upvote_tip'),  # Ruta para upvote
    path('<int:tip_id>/downvote/', downvote_tip, name='downvote_tip'),  # Ruta para downvote

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

    # Listado de usuarios con reputación
    path('users/list/', users_list, name='users_list'),  # Nueva ruta añadida

    # Ruta para probar la página 404
    path('test-404/', test_404_view, name='test_404'),
]