from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tips import views  # Importa las vistas desde el módulo tips

# Configuración del manejador de errores 404
handler404 = 'tips.views.custom_404_view'

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls, name='admin'),

    # Página de inicio (Home)
    path('', views.home, name='home'),

    # Incluir las rutas de tips
    path('tips/', include('tips.urls')),

    # Rutas de autenticación
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # Login
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),  # Logout
    path("register/", views.register, name="register"),  # Registro de usuarios

    # Rutas para restablecimiento de contraseñas
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]

# Agregar archivos estáticos si corresponde
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)