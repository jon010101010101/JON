from pathlib import Path
import os
from decouple import config

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (no exponer en producción)
SECRET_KEY = config('SECRET_KEY', default='clave_secreta_de_respaldo')

# Depuración (cambiar a False en producción)
DEBUG = config('DEBUG', default=True, cast=bool)

print(f"DEBUG={DEBUG}")  # Esto imprimirá el valor de DEBUG en la consola

# Hosts permitidos (desde .env)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')

# Configuración del usuario
AUTH_USER_MODEL = 'ex06.tips.CustomUser'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = '/login/'  # Redirección para vistas protegidas

# Configuración de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ex06.tips',
    'bootstrap5',
    'axes',  # Protección contra ataques de fuerza bruta
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',  # Integración con django-axes
]

# Configuración de backends de autenticación
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # Requerido por django-axes
    'django.contrib.auth.backends.ModelBackend',  # Backend predeterminado de Django
]

# Configuración de django-axes
AXES_FAILURE_LIMIT = 5  # Intentos fallidos permitidos
AXES_COOLOFF_TIME = 1  # Tiempo de bloqueo en horas
AXES_LOCKOUT_TEMPLATE = 'registration/lockout.html'
AXES_RESET_ON_SUCCESS = True  # Restablecer en inicio exitoso

# Configuración de URLs
ROOT_URLCONF = 'ex06.urls'
handler404 = 'tips.views.custom_404_view'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'ex06', 'templates')],  # Incluye la ruta correcta
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración del servidor WSGI
WSGI_APPLICATION = 'ex06.wsgi.application'

# Configuración de base de datos (actualmente SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Esto debe apuntar al directorio donde está tu carpeta "static"
]
#STATIC_ROOT = BASE_DIR / "staticfiles"  # Esto define dónde se copiarán los archivos 
# con collectstatic. ejecutamos python manage.py collectstatic

# Configuración del correo gmail (desde .env)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# Configuración de claves automáticas
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'