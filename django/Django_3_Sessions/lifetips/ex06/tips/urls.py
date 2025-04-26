from django.urls import path
from django.contrib.auth import views as auth_views  # Importar vistas genéricas de autenticación
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),  # Página de inicio
    
    # Funciones relacionadas con los tips
    path('create/', views.create_tip, name='create_tip'),  # Crear nuevo tip
    path('<int:tip_id>/upvote/', views.upvote_tip, name='upvote_tip'),  # Votar positivo en tip
    path('<int:tip_id>/downvote/', views.downvote_tip, name='downvote_tip'),  # Votar negativo en tip
    path('<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),  # Eliminar un tip
    path('list/', views.tips_list, name='tips_list'),  # Listar tips
    
    # Registro de nuevos usuarios
    path("register/", views.register, name="register"),  # Página de registro
    
    # Login y Logout
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Plantilla de login
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),  # Redirige al home después del logout

    # Recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Iniciar proceso de restablecimiento
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Confirmación de envío del correo
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Confirmar nueva contraseña
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Contraseña restablecida correctamente
]
