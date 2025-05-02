from pathlib import Path
import os
from dotenv import load_dotenv
from decouple import Config, RepositoryEnv

# Rutas base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar las variables de entorno desde el archivo .env_lifetips
load_dotenv('/sgoinfre/.env_lifetips')

# Cargar variables de entorno desde un archivo externo usando python-decouple
ENV_FILE = os.path.expanduser('/home/jurrutia/sgoinfre/.env_lifetips')
config = Config(RepositoryEnv(ENV_FILE))

# Clave secreta (no exponer en producción)
SECRET_KEY = os.getenv('SECRET_KEY', config("SECRET_KEY", default='clave_secreta_de_respaldo'))

# Depuración (cambiar a False en producción)
DEBUG = os.getenv('DEBUG', config("DEBUG", default='False')) == 'True'

# Hosts permitidos
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', config("ALLOWED_HOSTS", default='127.0.0.1,localhost')).split(',')

# Configuración del usuario
AUTH_USER_MODEL = 'tips.CustomUser'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = '/login/'  # Redirección para vistas protegidas

# Configuración del Test Runner personalizado
TEST_RUNNER = "custom_test_runner.CustomTestRunner"

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tips',
    'bootstrap5',
    'axes',  # Protección contra ataques de fuerza bruta
    'django_extensions',
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

# Backends de autenticación
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

# Configuración del tiempo de expiración del token de restablecimiento de contraseña
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 365 * 10  # 10 años en segundos

# Internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Carpeta para tus propios archivos estáticos (si existe)
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Carpeta donde `collectstatic` recopila los archivos estáticos

# Configuración del correo usando SendGrid
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Siempre 'apikey' para SendGrid
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='lifetipsdjango@gmail.com')

# Configuración del dominio y protocolo para correos electrónicos
EMAIL_PROTOCOL = os.getenv('EMAIL_PROTOCOL', config('EMAIL_PROTOCOL', default='http'))  # Puede ser 'http' o 'https'
EMAIL_DOMAIN = os.getenv('EMAIL_DOMAIN', config('EMAIL_DOMAIN', default='127.0.0.1:8000'))

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'WARNING',  # Cambiar los mensajes DEBUG a WARNING
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'tips.signals': {  # Configuración específica para tips.signals
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

# Configuración de claves automáticas
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'