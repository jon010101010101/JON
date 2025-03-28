# DOCKERS

*1.Instalar Docker*
Si Docker no está instalado, descárgalo desde su página oficial (https://www.docker.com/) e instálalo. En Windows y macOS, puedes usar Docker Desktop; en Linux, asegúrate de que tu usuario tenga acceso a Docker sin necesidad de permisos sudo.

*2. Descargar la imagen oficial de PostgreSQL*
Ejecuta el siguiente comando en la terminal para descargar la imagen oficial de PostgreSQL desde Docker Hub:

docker pull postgres

*3. Crear y ejecutar el contenedor*
Para iniciar el contenedor con PostgreSQL, usa el siguiente comando:

docker run --name my-postgres-container \
-e POSTGRES_USER=myuser \
-e POSTGRES_PASSWORD=mypassword \
-e POSTGRES_DB=mydatabase \
-p 5432:5432 \
-d postgres

Explicación:

--name my-postgres-container: Nombre del contenedor.

-e POSTGRES_USER=myuser: Usuario de la base de datos.

-e POSTGRES_PASSWORD=mypassword: Contraseña del usuario.

-e POSTGRES_DB=mydatabase: Nombre de la base de datos inicial.

-p 5432:5432: Mapea el puerto 5432 del contenedor al puerto 5432 de tu máquina local.

-d postgres: Ejecuta el contenedor en segundo plano utilizando la imagen postgres.

*4. Verificar que el contenedor está funcionando*
Ejecuta el siguiente comando para listar los contenedores activos:

docker ps
Deberías ver tu contenedor listado con su estado como "running".

*5. Conectarse al servidor PostgreSQL*
Puedes conectarte al servidor PostgreSQL dentro del contenedor usando el cliente psql o herramientas externas como DBeaver o pgAdmin.

Para usar psql desde el propio contenedor, ejecuta:

docker exec -it my-postgres-container psql -U myuser -d mydatabase

Esto abrirá una sesión interactiva con tu base de datos.

*6. Persistencia de datos (opcional)*
Si necesitas que los datos persistan incluso después de detener o eliminar el contenedor, utiliza volúmenes:

docker run --name my-postgres-container \
-e POSTGRES_USER=myuser \
-e POSTGRES_PASSWORD=mypassword \
-e POSTGRES_DB=mydatabase \
-p 5432:5432 \
-v /path/to/local/folder:/var/lib/postgresql/data \
-d postgres
El volumen asegura que los datos se guarden en /path/to/local/folder en tu máquina local.

*7. Detener y eliminar el contenedor*
Para detener el contenedor:

docker stop my-postgres-container

Para eliminarlo:

docker rm my-postgres-container

*Ventajas de usar Docker con PostgreSQL*

No requiere instalación local ni permisos elevados.

Fácil configuración y eliminación.

Aislamiento completo del entorno.

Portabilidad entre sistemas.

Este enfoque es ideal para desarrollo y pruebas rápidas sin alterar tu sistema operativo.

cd
docker stop my-postgres-container

*para salir \q*

*para levantar docker*
docker start my-postgres-container



# EJERCICIO 00

**Creación del proyecto Django:**

django-admin startproject d42
cd d42

**Creación de la aplicación ex00:**

python manage.py startapp ex00

**Configuración de Docker:**

Creamos un archivo Dockerfile en la raíz del proyecto.

Creamos un archivo docker-compose.yml para definir los servicios (Django y PostgreSQL).

Configuración de requirements.txt:
Creamos un archivo requirements.txt en la raíz del proyecto con las dependencias necesarias:

Django==4.2
psycopg2-binary==2.9.6

**Configuración de la base de datos en settings.py:**
Modificamos la configuración de la base de datos para usar PostgreSQL.

Creación y aplicación de las migraciones iniciales:

python manage.py makemigrations
python manage.py migrate

**Levantamiento de los contenedores Docker:**

docker-compose up -d

**Estructura del proyecto:**

text
ex00/
├── d42/
│   ├── d42/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── ex00/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   └── db.sqlite3
└── requirements.txt

**Contenido de los archivos principales:**

*1.- d42/d42/settings.py (añadir a INSTALLED_APPS):*


INSTALLED_APPS = [
    # ...
    'ex00',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

*2.- d42/d42/urls.py:*

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', include('ex00.urls')),
]

*3.- d42/ex00/urls.py:*

from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init, name='init'),
]

*4.-d42/ex00/views.py:*

from django.http import HttpResponse
import psycopg2

def init(request):
    try:
        conn = psycopg2.connect(
            dbname='mydatabase',
            user='myuser',
            password='mypassword',
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            )
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

**Pasos de ejecución:**

*1.-Asegurarse de que Docker está corriendo con PostgreSQL:*

docker run --name my-postgres-container -e POSTGRES_PASSWORD=mypassword -e POSTGRES_USER=myuser -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres

*2.-Instalar las dependencias:*

pip install django psycopg2-binary

*3.-Ejecutar las migraciones:*

python manage.py migrate

*3.-Iniciar el servidor de desarrollo:*

python manage.py runserver

*4.-Acceder a la URL:*
http://127.0.0.1:8000/ex00/init/

*5.-Verificar la creación de la tabla:*

docker exec -it my-postgres-container psql -U myuser -d mydatabase

Dentro de psql:

sql
\d ex00_movies
\q

*En la web tiene que poner OK*


*Comprobarción de que ha realizado la estructura en SQL*
 d42 git:(main) ✗ docker exec -it my-postgres-container psql -U myuser -d mydatabase

psql (17.4 (Debian 17.4-1.pgdg120+2))
Type "help" for help.

mydatabase=# \d ex00_movies
                       Table "public.ex00_movies"
    Column     |          Type          | Collation | Nullable | Default 
---------------+------------------------+-----------+----------+---------
 title         | character varying(64)  |           | not null | 
 episode_nb    | integer                |           | not null | 
 opening_crawl | text                   |           |          | 
 director      | character varying(32)  |           | not null | 
 producer      | character varying(128) |           | not null | 
 release_date  | date                   |           | not null | 
Indexes:
    "ex00_movies_pkey" PRIMARY KEY, btree (episode_nb)
    "ex00_movies_title_key" UNIQUE CONSTRAINT, btree (title)

mydatabase=# \q

# EJERCICIO 01