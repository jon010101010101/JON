from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from tips import views  # Importa las vistas desde el módulo tips
from tips.reset_password_flow_test import send_reset_email

# Configuración del manejador de errores 404
def test_404_view(request):
    return render(request, '404.html', status=404)


# Configuración de las URLs principales
urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls, name='admin'),

    # Página de inicio (Home)
    path('', views.home, name='home'),

    # Incluir las rutas de tips
    path('tips/', include('tips.urls')),

    # Ruta para probar la página 404
    path('test-404/', test_404_view, name='test_404'),

    # Rutas de autenticación
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.register, name="register"),

    # Rutas para restablecimiento de contraseñas
    path(
        'password_reset/',
        views.CustomPasswordResetView.as_view(
            template_name='registration/password_reset.html',
            email_template_name='registration/password_reset_email.txt',
            subject_template_name='registration/password_reset_subject.txt',
        ),
        name='password_reset',
    ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset_done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),

    # Ruta para enviar correos de restablecimiento de contraseña
    path('send-reset-email/<str:user_email>/', send_reset_email, name='send_reset_email'),
]

# Configuración para servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)