from django.urls import path
from django.contrib.auth import views as auth_views  # Importar vistas genéricas de autenticación
from . import views
from .views import CustomPasswordResetView  # Importar la nueva vista personalizada

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),  # Página de inicio

    # Funciones relacionadas con los tips
    path('create/', views.create_tip, name='create_tip'),  # Crear nuevo tip
    path('<int:tip_id>/vote/<str:vote_type>/', views.vote_tip, name='vote_tip'), # Votar
    path('<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),  # Eliminar un tip
<<<<<<< HEAD
=======
    path('list/', views.tips_list, name='tips_list'),  # Listar tips
>>>>>>> aa7cf094 (Remove unused files and clean up project)

    # Registro de nuevos usuarios
    path("register/", views.register, name="register"),  # Página de registro

    # Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Plantilla de login
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),  # Redirige al home después del logout

    # Recuperación de contraseña con plantillas personalizadas
    path(
        'password_reset/', 
        CustomPasswordResetView.as_view(template_name='registration/password_reset.html'),  # Usar la vista personalizada
        name='password_reset'
    ),  # Iniciar proceso de restablecimiento
    path(
        'password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
        name='password_reset_done'
    ),  # Confirmación de envío del correo
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name='password_reset_confirm'
    ),  # Confirmar nueva contraseña
    path(
        'reset_done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
        name='password_reset_complete'
    ),  # Contraseña restablecida correctamente
]