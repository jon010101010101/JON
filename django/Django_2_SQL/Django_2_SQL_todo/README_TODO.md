# Requisitos Previos
Máquina Virtual: Una máquina virtual configurada correctamente con Python 3 y PostgreSQL instalado.

PostgreSQL: Servidor PostgreSQL instalado y en ejecución. Dado que no tienes acceso a sudo, deberás utilizar una instalación local o una instancia remota.

Conda: Conda instalado y configurado como gestor de entornos.

# II. Configuración del Proyecto
Crear el Proyecto Django:

mkdir <tu_nombre>
cd <tu_nombre>
conda create -n venv python=3.9  # Reemplaza 3.9 con la versión de Python que uses
conda activate venv
pip install django psycopg2
django-admin startproject d42  # Reemplaza d42 con el día actual
cd d42

**Configurar la Base de Datos PostgreSQL:**

Importante: Dado que no tienes acceso a sudo, necesitarás una instancia de PostgreSQL a la que puedas acceder sin privilegios elevados. Esto podría ser:

Una instalación local en tu directorio de usuario (si es posible).

Una instancia remota proporcionada por un servicio.

Crear la base de datos y el usuario (esto puede variar dependiendo de tu configuración):

Si tienes acceso a la línea de comandos de PostgreSQL (ej., psql), y tienes los permisos necesarios, puedes crear la base de datos y el usuario de la siguiente manera:

psql -U <usuario_con_permisos> -d postgres
CREATE DATABASE djangotraining;
CREATE USER djangouser WITH PASSWORD 'secret';
ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE djangotraining TO djangouser;
\q
Reemplaza <usuario_con_permisos> con un usuario que tenga los permisos para crear bases de datos y usuarios en tu instancia de PostgreSQL.

Modificar settings.py:

python
# settings.py (ejemplo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangotraining',
        'USER': 'djangouser',
        'PASSWORD': 'secret',
        'HOST': 'localhost',  # O la dirección del servidor remoto
        'PORT': '5432',  # O el puerto si es diferente
    }
}
Asegúrate de que HOST y PORT reflejen la ubicación de tu instancia de PostgreSQL.

Verificar la Conexión a la Base de Datos:

Ejecutar python3 manage.py check

# III. Estructura del Proyecto
text
|-- <tu_nombre>
|   |-- .
|   |-- ..
|   |-- .git
|   |-- .gitignore
|   |-- d42  # Nombre del proyecto (reemplaza d42)
|   |   |-- __init__.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|   |-- ex00
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- forms.py
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- tests.py
|   |   |-- urls.py
|   |   |-- views.py
|   |-- ex01
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- forms.py
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- tests.py
|   |   |-- urls.py
|   |   |-- views.py
|   |-- ... (ex02 - ex08)
|   |-- ex10
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- forms.py
|   |   |-- __init__.py
|   |   |-- models.py
|   |   |-- tests.py
|   |   |-- urls.py
|   |   |-- views.py
|   |-- manage.py
IV. Instrucciones Específicas del Ejercicio
Recuerda:

Cada ejercicio es independiente. Duplica el código necesario en cada uno.

Usa estilos en línea para la consistencia visual.

Presta atención a si debes usar el ORM o SQL.

No incluyas archivos de migración.

Disclaimer: No information regarding ex09 was provided, therefore it will not be included in the project.

# Ejercicio 00: SQL - Creación de una Tabla

Directorio: ex00/

Archivos a Entregar: ex00/views.py

Requisitos:

Crear una tabla llamada ex00_movies con los siguientes campos:

title: VARCHAR(64) UNIQUE NOT NULL

episode_nb: INTEGER PRIMARY KEY

opening_crawl: TEXT

director: VARCHAR(32) NOT NULL

producer: VARCHAR(128) NOT NULL

release_date: DATE NOT NULL

Acceder a la vista en 127.0.0.1:8000/ex00/init.

Código de ejemplo (ex00/views.py):

from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
Verificación:

Accede a 127.0.0.1:8000/ex00/init. Debe mostrar "OK" o un mensaje de error.

# Ejercicio 01: ORM - Creación de una Tabla

Directorio: ex01/

Archivos a Entregar: ex01/models.py

Requisitos:

Crear un modelo Django llamado Movies con los mismos campos que en el Ejercicio 00.

El modelo debe tener un método __str__ que devuelva el título.

Código de ejemplo (ex01/models.py):

from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    def __str__(self):
        return self.title
Comandos:

python3 manage.py makemigrations ex01
python3 manage.py migrate
Verificación: Abre el shell de Django (python3 manage.py shell) e intenta crear una instancia del modelo Movies.

# Ejercicio 02: SQL - Inserción de Datos

Directorio: ex02/

Archivos a Entregar: ex02/views.py

Requisitos:

Crear una tabla llamada ex02_movies.

Insertar los siguientes datos:

episode_nb: 1 - title: The Phantom Menace - director: George Lucas - producer: Rick McCallum - release_date: 1999-05-19

episode_nb: 2 - title: Attack of the Clones - director: George Lucas - producer: Rick McCallum - release_date: 2002-05-16

episode_nb: 3 - title: Revenge of the Sith - director: George Lucas - producer: Rick McCallum - release_date: 2005-05-19

episode_nb: 4 - title: A New Hope - director: George Lucas - producer: Gary Kurtz, Rick McCallum - release_date: 1977-05-25

episode_nb: 5 - title: The Empire Strikes Back - director: Irvin Kershner - producer: Gary Kurtz, Rick McCallum - release_date: 1980-05-17

episode_nb: 6 - title: Return of the Jedi - director: Richard Marquand - producer: Howard G. Kazanjian, George Lucas, Rick McCallum - release_date: 1983-05-25

episode_nb: 7 - title: The Force Awakens - director: J. J. Abrams - producer: Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date: 2015-12-11

Crear vistas en /ex02/init, /ex02/populate, y /ex02/display.

Código de ejemplo (ex02/views.py):

from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def populate(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        # Insertar los datos (ejemplo)
        cursor.execute("""
            INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
            VALUES (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19');
        """)
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ex02_movies;")
        rows = cursor.fetchall()

        # Generar la tabla HTML (con estilos en línea)
        html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr></thead><tbody>"
        for row in rows:
            html += f"<tr><td style='border: 1px solid black;'>{row[0]}</td><td style='border: 1px solid black;'>{row[1]}</td><td style='border: 1px solid black;'>{row[2]}</td><td style='border: 1px solid black;'>{row[3]}</td><td style='border: 1px solid black;'>{row[4]}</td></tr>"
        html += "</tbody></table>"
        return HttpResponse(html)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
Verificación:

Accede a /ex02/init y /ex02/populate. Deben mostrar "OK" (o un mensaje de error).

Accede a /ex02/display. Debe mostrar una tabla HTML con los datos.

# Ejercicio 03: ORM - Inserción de Datos

Directorio: ex03/

Archivos a Entregar: ex03/models.py, ex03/views.py

Requisitos:

Crear un modelo Django idéntico al del Ejercicio 01.

Insertar los mismos datos que en el Ejercicio 02 usando el ORM.

Crear vistas en /ex03/populate y /ex03/display.

Código de ejemplo (ex03/views.py):

from django.http import HttpResponse
from .models import Movies

def populate(request):
    try:
        Movies.objects.create(episode_nb=1, title='The Phantom Menace', director='George Lucas', producer='Rick McCallum', release_date='1999-05-19')
        Movies.objects.create(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16')
        Movies.objects.create(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer='Rick McCallum', release_date='2005-05-19')
        Movies.objects.create(episode_nb=4, title='A New Hope', director='George Lucas', producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25')
        Movies.objects.create(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17')
        Movies.objects.create(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25')
        Movies.objects.create(episode_nb=7, title='The Force Awakens', director='J. J. Abrams', producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    movies = Movies.objects.all()
    html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr></thead><tbody>"
    for movie in movies:
        html += f"<tr><td style='border: 1px solid black;'>{movie.episode_nb}</td><td style='border: 1px solid black;'>{movie.title}</td><td style='border: 1px solid black;'>{movie.director}</td><td style='border: 1px solid black;'>{movie.producer}</td><td style='border: 1px solid black;'>{movie.release_date}</td></tr>"
    html += "</tbody></table>"
    return HttpResponse(html)
Comandos:

python3 manage.py makemigrations ex03
python3 manage.py migrate
Verificación:

Acceder a /ex03/populate debe mostrar "OK" (o un mensaje de error).

Acceder a /ex03/display debe mostrar una tabla HTML con los datos.

# Ejercicio 04: SQL - Eliminación de Datos

Directorio: ex04/

Archivos a Entregar: ex04/views.py, ex04/templates/ex04/remove.html

Requisitos:

Crear una tabla llamada ex04_movies.

Insertar los datos de las películas.

Implementar la funcionalidad "remove" para eliminar películas de la base de datos.

Crear una vista /ex04/remove que muestre un formulario HTML con una lista desplegable de títulos y un botón "remove".

Código de ejemplo (ex04/views.py):

from django.http import HttpResponse
import psycopg2
from django.conf import settings
from django.shortcuts import render

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
def populate(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        # Insertar los datos
        movies = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
        ]
        for movie in movies:
            cursor.execute("""
                INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s);
            """, movie)
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ex04_movies;")
        rows = cursor.fetchall()

        html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr></thead><tbody>"
        for row in rows:
            html += f"<tr><td style='border: 1px solid black;'>{row[0]}</td><td style='border: 1px solid black;'>{row[1]}</td><td style='border: 1px solid black;'>{row[2]}</td><td style='border: 1px solid black;'>{row[3]}</td><td style='border: 1px solid black;'>{row[4]}</td></tr>"
        html += "</tbody></table>"
        return HttpResponse(html)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def remove(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        if request.method == 'POST':
            title_to_remove = request.POST.get('title')
            cursor.execute("DELETE FROM ex04_movies WHERE title = %s;", (title_to_remove,))
            conn.commit()

        cursor.execute("SELECT title FROM ex04_movies;")
        movies = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return render(request, 'ex04/remove.html', {'movies': movies})

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
Código de ejemplo (ex04/templates/ex04/remove.html):

xml
<!DOCTYPE html>
<html>
<head>
    <title>Remove Movie</title>
</head>
<body>
    <h1>Remove Movie</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Select movie to remove:</label>
        <select name="title" id="title">
            {% for movie in movies %}
                <option value="{{ movie }}">{{ movie }}</option>
            {% endfor %}
        </select>
        <button type="submit">Remove</button>
    </form>
</body>
</html>
Verificación:

Accede a /ex04/remove. Debe mostrar un formulario con la lista de películas.

Al seleccionar una película y hacer clic en "Remove", la película debe ser eliminada de la tabla.

# Ejercicio 05: ORM - Eliminación de Datos

Directorio: ex05/

Archivos a Entregar: ex05/models.py, ex05/views.py, ex05/templates/ex05/remove.html

Requisitos:

Crear un modelo Django idéntico al del Ejercicio 01.

Implementar la funcionalidad "remove" usando el ORM.

Crear una vista /ex05/remove que muestre un formulario HTML con una lista desplegable de títulos y un botón "remove".

Código de ejemplo (ex05/views.py):

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies

def populate(request):
    try:
        Movies.objects.create(episode_nb=1, title='The Phantom Menace', director='George Lucas', producer='Rick McCallum', release_date='1999-05-19')
        Movies.objects.create(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16')
        Movies.objects.create(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer='Rick McCallum', release_date='2005-05-19')
        Movies.objects.create(episode_nb=4, title='A New Hope', director='George Lucas', producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25')
        Movies.objects.create(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17')
        Movies.objects.create(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25')
        Movies.objects.create(episode_nb=7, title='The Force Awakens', director='J. J. Abrams', producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    movies = Movies.objects.all()
    html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr></thead><tbody>"
    for movie in movies:
        html += f"<tr><td style='border: 1px solid black;'>{movie.episode_nb}</td><td style='border: 1px solid black;'>{movie.title}</td><td style='border: 1px solid black;'>{movie.director}</td><td style='border: 1px solid black;'>{movie.producer}</td><td style='border: 1px solid black;'>{movie.release_date}</td></tr>"
    html += "</tbody></table>"
    return HttpResponse(html)

def remove(request):
    movies = Movies.objects.all()
    if request.method == 'POST':
        title_to_remove = request.POST.get('title')
        Movies.objects.filter(title=title_to_remove).delete()
        return redirect('ex05:remove')

    return render(request, 'ex05/remove.html', {'movies': movies})
Código de ejemplo (ex05/templates/ex05/remove.html):

xml
<!DOCTYPE html>
<html>
<head>
    <title>Remove Movie</title>
</head>
<body>
    <h1>Remove Movie</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Select movie to remove:</label>
        <select name="title" id="title">
            {% for movie in movies %}
                <option value="{{ movie.title }}">{{ movie.title }}</option>
            {% endfor %}
        </select>
        <button type="submit">Remove</button>
    </form>
</body>
</html>
Comandos:

python3 manage.py makemigrations ex05
python3 manage.py migrate
Verificación:

Accede a /ex05/remove. Debe mostrar un formulario con la lista de películas.

Al seleccionar una película y hacer clic en "Remove", la película debe ser eliminada de la tabla.

# Ejercicio 06: SQL - Actualización de Datos

Directorio: ex06/

Archivos a Entregar: ex06/views.py, ex06/templates/ex06/update.html

Requisitos:

Crear una tabla llamada ex06_movies con los campos adicionales created y updated.

Implementar la funcionalidad de actualización del campo opening_crawl.

Crear una vista /ex06/update que permita seleccionar una película y actualizar su opening_crawl.

Código de ejemplo (ex06/views.py):

from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex06_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT NOW(),
                updated TIMESTAMP NOT NULL DEFAULT NOW()
            );

            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            RETURN NEW;
            END;
            $$ language 'plpgsql';

            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
def populate(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        # Insertar los datos
        movies = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19', 'This is the opening crawl.'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16', 'This is the opening crawl.'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19', 'This is the opening crawl.'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25', 'This is the opening crawl.'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17', 'This is the opening crawl.'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25', 'This is the opening crawl.'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11', 'This is the opening crawl.')
        ]
        for movie in movies:
            cursor.execute("""
                INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date, opening_crawl)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ex06_movies;")
        rows = cursor.fetchall()

        html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Opening Crawl</th><th>Created</th><th>Updated</th></tr></thead><tbody>"
        for row in rows:
            html += f"<tr><td style='border: 1px solid black;'>{row[0]}</td><td style='border: 1px solid black;'>{row[1]}</td><td style='border: 1px solid black;'>{row[2]}</td><td style='border: 1px solid black;'>{row[3]}</td><td style='border: 1px solid black;'>{row[4]}</td><td style='border: 1px solid black;'>{row[5]}</td><td style='border: 1px solid black;'>{row[6]}</td><td style='border: 1px solid black;'>{row[7]}</td></tr>"
        html += "</tbody></table>"
        return HttpResponse(html)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def update(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        if request.method == 'POST':
            title_to_update = request.POST.get('title')
            new_opening_crawl = request.POST.get('opening_crawl')
            cursor.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s;", (new_opening_crawl, title_to_update))
            conn.commit()

        cursor.execute("SELECT title FROM ex06_movies;")
        movies = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return render(request, 'ex06/update.html', {'movies': movies})

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
Código de ejemplo (ex06/templates/ex06/update.html):

xml
<!DOCTYPE html>
<html>
<head>
    <title>Update Movie</title>
</head>
<body>
    <h1>Update Movie</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Select movie to update:</label>
        <select name="title" id="title">
            {% for movie in movies %}
                <option value="{{ movie }}">{{ movie }}</option>
            {% endfor %}
        </select>
        <label for="opening_crawl">New opening crawl:</label>
        <textarea name="opening_crawl" id="opening_crawl" rows="4" cols="50"></textarea>
        <button type="submit">Update</button>
    </form>
</body>
</html>
Verificación:

Acceder a /ex06/update debe mostrar un formulario con la lista de películas y un campo de texto para el opening crawl.

Al seleccionar una película y actualizar el opening crawl, la tabla debe reflejar el cambio.

# Ejercicio 07: ORM - Actualización de Datos

Directorio: ex07/

Archivos a Entregar: ex07/models.py, ex07/views.py, ex07/templates/ex07/update.html

Requisitos:

Crear un modelo Django con los campos created y updated.

Implementar la funcionalidad de actualización del campo opening_crawl usando el ORM.

Crear una vista /ex07/update que permita seleccionar una película y actualizar su opening_crawl.

Código de ejemplo (ex07/models.py):

from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
Código de ejemplo (ex07/views.py):

python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies

def populate(request):
    try:
        Movies.objects.create(episode_nb=1, title='The Phantom Menace', director='George Lucas', producer='Rick McCallum', release_date='1999-05-19', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer='Rick McCallum', release_date='2002-05-16', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer='Rick McCallum', release_date='2005-05-19', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=4, title='A New Hope', director='George Lucas', producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25', opening_crawl='This is the opening crawl.')
        Movies.objects.create(episode_nb=7, title='The Force Awakens', director='J. J. Abrams', producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11', opening_crawl='This is the opening crawl.')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    movies = Movies.objects.all()
    html = "<table style='width:100%; border-collapse: collapse;'><thead><tr><th>Episode Nb</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th><th>Opening Crawl</th><th>Created</th><th>Updated</th></tr></thead><tbody>"
    for movie in movies:
        html += f"<tr><td style='border: 1px solid black;'>{movie.episode_nb}</td><td style='border: 1px solid black;'>{movie.title}</td><td style='border: 1px solid black;'>{movie.director}</td><td style='border: 1px solid black;'>{movie.producer}</td><td style='border: 1px solid black;'>{movie.release_date}</td><td style='border: 1px solid black;'>{movie.opening_crawl}</td><td style='border: 1px solid black;'>{movie.created}</td><td style='border: 1px solid black;'>{movie.updated}</td></tr>"
    html += "</tbody></table>"
    return HttpResponse(html)

def update(request):
    movies = Movies.objects.all()
    if request.method == 'POST':
        title_to_update = request.POST.get('title')
        new_opening_crawl = request.POST.get('opening_crawl')
        movie = Movies.objects.get(title=title_to_update)
        movie.opening_crawl = new_opening_crawl
        movie.save()
        return redirect('ex07:update')

    return render(request, 'ex07/update.html', {'movies': movies})
Código de ejemplo (ex07/templates/ex07/update.html):

xml
<!DOCTYPE html>
<html>
<head>
    <title>Update Movie</title>
</head>
<body>
    <h1>Update Movie</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Select movie to update:</label>
        <select name="title" id="title">
            {% for movie in movies %}
                <option value="{{ movie.title }}">{{ movie.title }}</option>
            {% endfor %}
        </select>
        <label for="opening_crawl">New opening crawl:</label>
        <textarea name="opening_crawl" id="opening_crawl" rows="4" cols="50"></textarea>
        <button type="submit">Update</button>
    </form>
</body>
</html>
Comandos:

python3 manage.py makemigrations ex07
python3 manage.py migrate
Verificación:

Acceder a /ex07/update debe mostrar un formulario con la lista de películas y un campo de texto para el opening crawl.

Al seleccionar una película y actualizar el opening crawl, la tabla debe reflejar el cambio y el campo updated debe actualizarse.

# Ejercicio 08: SQL - Clave Externa

Directorio: ex08/

Archivos a Entregar: ex08/views.py

Requisitos:

Crear dos tablas: ex08_planets y ex08_characters.

ex08_planets:

id: Serial, Primary Key

name: Unique, VARCHAR(64) NOT NULL

climate: VARCHAR(128)

terrain: VARCHAR(128)

ex08_characters:

id: Serial, Primary Key

planet_id: Integer, Foreign Key referencing ex08_planets.id

name: Unique, VARCHAR(64) NOT NULL

gender: Enum ("Male", "Female", "Other", "Unknown")

La vista /ex08/init debe crear estas tablas usando psycopg2.

Código de ejemplo (ex08/views.py):

from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(128),
                terrain VARCHAR(128)
            );

            CREATE TYPE gender_enum AS ENUM ('Male', 'Female', 'Other', 'Unknown');

            CREATE TABLE IF NOT EXISTS ex08_characters (
                id SERIAL PRIMARY KEY,
                planet_id INTEGER REFERENCES ex08_planets(id),
                name VARCHAR(64) UNIQUE NOT NULL,
                gender gender_enum
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
Verificación:

Accede a /ex08/init. Debe mostrar "OK" o un mensaje de error.

Verifica la estructura de las tablas en la base de datos.

# Ejercicio 09: ORM - Relaciones y Consultas

Directorio: ex09/

Archivos a Entregar: ex09/models.py, ex09/views.py, ex09/ex09_initial_data.json

Requisitos:

Crear dos modelos: Planets y People (ver especificaciones en la descripción del ejercicio).

El modelo Planets debe contener los siguientes campos:

name: unique, variable character chain, 64 byte maximum size, non null.

climate: variable character chain.

diameter: whole.

orbital_period: whole.

population: large whole.

rotation_period: whole.

surface_water: real.

terrain: character chains.

created a datetime type (date and time), that, when created, must automatically set to the current date and time.

updated a datetime type (date and time), that, when created, must automatically set to the current date and time and automatically updates with each update.

El modelo People debe contener los siguientes campos:

name: character chain, 64 byte maximum size, non null.

birth_year: character chain, 32 byte maximum size.

gender: character chain, 32 byte maximum size.

eye_color: character chain, 32 byte maximum size.

hair_color: character chain, 32 byte maximum size.

height: whole.

mass: real.

homeworld: character chain, 64 byte maximum size, foreign key referencing the name column of this app’s Planets table.

created a datetime type (date and time), that, when created, must automatically set to the current date and time.

updated a datetime type (date and time), that, when created, must automatically set to the current date and time and automatically updates with each update.

Crear una vista /ex09/display que muestre los nombres de los personajes, su planeta natal y el clima, ordenados alfabéticamente por nombre del personaje en una tabla HTML.

Filtrar los climas mostrados para que sólo se incluyan aquellos que sean "windy" o "moderately windy".

Crea un comando personalizado para cargar datos desde ex09_initial_data.json.

Código de ejemplo (ex09/models.py):

python
from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=128)
    diameter = models.IntegerField()
    orbital_period = models.IntegerField()
    population = models.CharField(max_length=64)  # Changed to CharField
    rotation_period = models.IntegerField()
    surface_water = models.FloatField()
    terrain = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    hair_color = models.CharField(max_length=32)
    height = models.IntegerField()
    mass = models.FloatField()
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, to_field='name')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
Código de ejemplo (ex09/views.py):

from django.shortcuts import render
from .models import Planets, People

def display(request):
    people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name')
    return render(request, 'ex09/display.html', {'people': people})
Código de ejemplo (ex09/templates/ex09/display.html):

xml
<!DOCTYPE html>
<html>
<head>
    <title>Star Wars Characters</title>
</head>
<body>
    <h1>Star Wars Characters</h1>
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="border: 1px solid black; padding: 8px;">Name</th>
                <th style="border: 1px solid black; padding: 8px;">Homeworld</th>
                <th style="border: 1px solid black; padding: 8px;">Climate</th>
            </tr>
        </thead>
        <tbody>
            {% for person in people %}
            <tr>
                <td style="border: 1px solid black; padding: 8px;">{{ person.name }}</td>
                <td style="border: 1px solid black; padding: 8px;">{{ person.homeworld.name }}</td>
                <td style="border: 1px solid black; padding: 8px;">{{ person.homeworld.climate }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
Código de ejemplo (ex09/management/commands/load_data.py):

import json
from django.core.management.base import BaseCommand
from ex09.models import Planets, People

class Command(BaseCommand):
    help = 'Load data from ex09_initial_data.json'

    def handle(self, *args, **kwargs):
        with open('ex09_initial_data.json', 'r') as f:
            data = json.load(f)

        for planet_data in data['planets']:
            planet, created = Planets.objects.get_or_create(
                name=planet_data['name'],
                defaults={
                    'climate': planet_data['climate'],
                    'diameter': planet_data['diameter'],
                    'orbital_period': planet_data['orbital_period'],
                    'population': planet_data['population'],
                    'rotation_period': planet_data['rotation_period'],
                    'surface_water': planet_data['surface_water'],
                    'terrain': planet_data['terrain'],
                }
            )

        for person_data in data['people']:
            planet = Planets.objects.get(name=person_data['homeworld'])
            person = People.objects.create(
                name=person_data['name'],
                birth_year=person_data['birth_year'],
                gender=person_data['gender'],
                eye_color=person_data['eye_color'],
                hair_color=person_data['hair_color'],
                height=person_data['height'],
                mass=person_data['mass'],
                homeworld=planet,
            )
Crea un directorio ex09/management/commands/ y coloca el archivo load_data.py allí.

Asegúrate de que el archivo ex09_initial_data.json esté en el directorio raíz de tu proyecto.

Ejecuta el comando para cargar los datos:

bash
python3 manage.py load_data
Comandos:

bash
python3 manage.py makemigrations ex09
python3 manage.py migrate
python3 manage.py runserver
Verificación:

Acceder a /ex09/display debe mostrar una tabla HTML con los datos filtrados y ordenados correctamente.

# Ejercicio 10: Búsqueda Avanzada

Directorio: ex10/

Archivos a Entregar: ex10/views.py, ex10/templates/ex10/search.html, ex10/models.py

Requisitos:

Crear Modelos Django:

Crear un modelo Planet con campos name (VARCHAR), climate (VARCHAR), y terrain (VARCHAR).

Crear un modelo People con campos name (VARCHAR), gender (enum), y una clave foránea homeworld referenciando el modelo Planet.

Crear una vista en /ex10/search que permita a los usuarios buscar nombres de personas o planetas.

La búsqueda debe ser insensible a mayúsculas y minúsculas.

Los resultados deben mostrar el nombre de la persona y el nombre de su planeta de origen.

Código de ejemplo (ex10/models.py):

from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=128)
    terrain = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class People(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown'),
    ]
    name = models.CharField(max_length=64, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
Código de ejemplo (ex10/views.py):

python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Planet, People
from django.db.models import Q

def search(request):
    query = request.GET.get('search')
    results = []

    if query:
        results = People.objects.filter(
            Q(name__icontains=query) |
            Q(homeworld__name__icontains=query)
        )

    context = {'results': results, 'query': query}
    return render(request, 'ex10/search.html', context)
Código de ejemplo (ex10/templates/ex10/search.html):

xml
<h1>Search</h1>
<form method="get">
    <input type="text" name="search" placeholder="Search People or Planets" value="{{ query }}">
    <button type="submit">Search</button>
</form>

<h2>Results</h2>
<ul>
    {% for person in results %}
    <li>{{ person.name }} - {{ person.homeworld.name }}</li>
    {% endfor %}
</ul>
Comandos:

python3 manage.py makemigrations ex10
python3 manage.py migrate
Verificación:

Accede a /ex10/search. Debe mostrar un formulario de búsqueda.

Ingresa un término de búsqueda y verifica que los resultados muestren las personas y planetas coincidentes.

V. Estilos CSS Consistentes (Estilos en Línea)
Para garantizar un aspecto coherente en toda la aplicación, utilice estilos CSS en línea directamente en las etiquetas HTML en sus plantillas.

Aquí tienes un ejemplo del estilo para una tabla:

xml
<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid black; padding: 8px;">Título</th>
      <th style="border: 1px solid black; padding: 8px;">Director</th>
      ...
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid black; padding: 8px;">...</td>
      <td style="border: 1px solid black; padding: 8px;">...</td>
      ...
    </tr>
  </tbody>
</table>