from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from tips import views  # Importa las vistas desde el módulo tips

# Configuración del manejador de errores 404
def test_404_view(request):
    return render(request, '404.html', status=404)

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls, name='admin'),

    # Página de inicio (Home)
    path('', views.home, name='home'),

    # Incluir las rutas de la app tips (donde están las rutas de password reset)
    path('tips/', include('tips.urls')),

    # Ruta para probar la página 404 (solo en desarrollo)
    path('test-404/', test_404_view, name='test_404'),

    # Rutas de autenticación globales (si quieres acceso directo desde raíz)
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),

    # Ruta para la verificación de 2FA
    path('verify-2fa/', views.verify_2fa, name='verify_2fa'),

    # Ruta de captcha
    path('captcha/', include('captcha.urls')),
]

handler404 = 'tips.views.custom_404_view'

# Configuración para servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


