
Dentro de cada directorio a entregar (ex00 a ex10)

* para crear la estructura del proyecto *
Este comando se utiliza para crear la estructura básica de un proyecto Django. Genera archivos como manage.py, settings.py, urls.py, etc., que son necesarios para configurar y gestionar el proyecto. Este comando debe ejecutarse una vez por proyecto, en el directorio donde quieres que se cree el proyecto.

django-admin startproject d00 .   
(el punto al final es importante para que no cree otra subcarpeta)


*Para crear la estructura de la app*
Este comando se utiliza para crear la estructura básica de una aplicación Django dentro del proyecto. Genera archivos como apps.py, views.py, models.py, etc., que son necesarios para desarrollar funcionalidades específicas dentro del proyecto. Este comando debe ejecutarse cada vez que quieras crear una nueva aplicación o funcionalidad.

python manage.py startapp ex00_app

estructura que se crea:

ex00/
├── manage.py                 # Archivo principal para comandos Django
├── d00_project/              # Configuración global del proyecto
│   ├── __init__.py
│   ├── settings.py           # Configuración global del proyecto
│   ├── urls.py               # URLs principales del proyecto
│   ├── wsgi.py
│   ├── asgi.py
├── ex00_app/                 # Aplicación específica para el ejercicio ex00
│   ├── __init__.py           # Archivo que define este módulo como paquete Python.
│   ├── admin.py              # Configuración del panel de administración (opcional).
│   ├── apps.py               # Configuración de la aplicación ex00_app.
│   ├── models.py             # Definición de modelos (opcional).
│   ├── tests.py              # Pruebas unitarias (opcional).
│   ├── views.py              # Lógica para las vistas del ejercicio ex00.

En d00/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ex00_app',  # Registrar la aplicación ex00_app.
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd00_project',  # Debe coincidir con POSTGRES_DB en docker-compose.yml
        'USER': 'djangouser',   # Debe coincidir con POSTGRES_USER en docker-compose.yml
        'PASSWORD': 'secret',   # Debe coincidir con POSTGRES_PASSWORD en docker-compose.yml
        'HOST': 'db',           # Nombre del servicio definido en docker-compose.yml
        'PORT': '5432',
    }
}


d00/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ex00_app.urls')),  # Conectar las URLs de ex00_app.
]

Crear archivo ex00_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init, name='init'),
]

ex00_app/views.py

from django.http import HttpResponse
import psycopg2

def init(request):
    try:
        # Conexión a la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname="d00_project",  # Nombre de la base de datos
            user="djangouser",     # Usuario de la base de datos
            password="secret",     # Contraseña del usuario
            host="db",             # Nombre del servicio definido en docker-compose.yml
            port="5432"            # Puerto de PostgreSQL
        )
        cursor = conn.cursor()

        # Crear una tabla si no existe
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()

        return HttpResponse("OK")  # Respuesta exitosa

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)  # Respuesta con error


Desde la raiz, para levantar el docker
docker-compose up --build


docker-compose down  # Detener y eliminar los contenedores existentes
docker-compose up --build  # Reconstruir y levantar los contenedores



find . -name \*.pyc -delete
find . -name __pycache__ -delete


Dentro del proyecto

iniciar servidor
pg_ctl -D ~/postgresql_data -l logfile start
verificar 
pg_ctl -D ~/postgresql_data status
para conectarse a la base de datos
psql -U djangouser -d d42
psql -U djangouser -d djangotraining
verificar el estadio del servicio
ps aux | grep postgres

python manage.py runserver

# pkill -f "python manage.py runserver"
# lsof -i :8000
# kill -9 38140

verificar que puerto esta oyendo
netstat -tuln | grep 5432



ex06 Comprobar que se ha cambiado metiendo el texto

python manage.py shell

from ex06.models import Movies

# Consulta todos los registros
movies = Movies.objects.all()

# Imprime el título y el contenido de cada película
for movie in movies:
    print(f"Title: {movie.title}\n{movie.opening_crawl}\n")


DELETE FROM django_migrations WHERE app = 'ex01';

DELETE FROM ex02_movies;

\d ex00_movies

* borrar migrations
djangotraining=# from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM django_migrations;")

* para verificar deberia salir 0 ......
djangotraining-# from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM django_migrations WHERE app = 'ex07';")
    count = cursor.fetchone()[0]  # Obtener el número directamente

print(count)  # Imprimir el número directamente