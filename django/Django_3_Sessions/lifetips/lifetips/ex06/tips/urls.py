from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from tips.views import (
    home,
    create_tip,
    tips_list,
    upvote_tip,
    downvote_tip,
    delete_tip,
    register,
    CustomPasswordResetView,
    reset_password,  # Vista personalizada para password_reset_confirm
    users_list,
    profile_edit,    # Vista de edición de perfil
    change_password, # Vista personalizada para cambio de contraseña
    user_reputation_report,  # <-- Añadimos aquí la nueva vista
)

# Vista para probar la página 404
def test_404_view(request):
    return render(request, '404.html', status=404)

urlpatterns = [
    # Página principal de la app (listado o inicio)
    path('', home, name='home'),

    # Funciones relacionadas con los tips
    path('create/', create_tip, name='create_tip'),
    path('list/', tips_list, name='tips_list'),
    path('<int:tip_id>/delete/', delete_tip, name='delete_tip'),
    path('<int:tip_id>/upvote/', upvote_tip, name='upvote_tip'),
    path('<int:tip_id>/downvote/', downvote_tip, name='downvote_tip'),

    # Registro de usuarios
    path("register/", register, name="register"),

    # Funciones de Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),

    # Recuperación de contraseña con vistas personalizadas
    path(
        'password_reset/',
        CustomPasswordResetView.as_view(
            template_name='registration/password_reset.html',
            email_template_name='registration/password_reset_email.txt',
            html_email_template_name='registration/password_reset_email.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        reset_password,  # Vista personalizada para password_reset_confirm
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    # Cambio de contraseña para usuarios autenticados (VISTA PERSONALIZADA)
    path('change-password/', change_password, name='change_password'),

    # Listado de usuarios con reputación
    path('users/list/', users_list, name='users_list'),

    # Edición de perfil de usuario autenticado
    path('profile/edit/', profile_edit, name='profile_edit'),

    # Informe de reputación de usuarios (NUEVA VISTA)
    path('reputation/', user_reputation_report, name='user_reputation_report'),

    # Ruta para probar la página 404
    path('test-404/', test_404_view, name='test_404'),
]
