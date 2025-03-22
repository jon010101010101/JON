Para crear un proyecto Django que muestre "¡Hola Mundo!" en http://localhost:8000/helloworld, sigue estos pasos:


**1. Crear el proyecto Django**
bash
django-admin startproject helloworld_project
cd helloworld_project
**2. Crear una aplicación dentro del proyecto**
bash
python manage.py startapp helloworld
**3. Configurar la aplicación en settings.py**
python
# Agregar la aplicación 'helloworld' a INSTALLED_APPS para que Django la reconozca.
INSTALLED_APPS = [
    ...
    'helloworld',
]
**4. Crear una vista en helloworld/views.py**
python
# Esta función devuelve un texto "Hello World!" como respuesta HTTP.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")
**5. Configurar las URLs de la aplicación en helloworld/urls.py**
python
# Aquí definimos las rutas específicas para la aplicación 'helloworld'.
from django.urls import path
from . import views

urlpatterns = [
    # La ruta raíz ('') llamará a la vista hello_world.
    path('', views.hello_world, name='hello_world'),
]
**6. Incluir las URLs de la aplicación en el proyecto principal (helloworld_project/urls.py)**
python
# Incluimos las URLs de la aplicación 'helloworld' en la ruta '/helloworld/'.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', include('helloworld.urls')),
]

**7. Generar migraciones**

*python manage.py makemigrations*

Ahora no es necesario hacerlo por que ya incluye la migraciones predefinidas, pero sino haria falta generar las migraciones, cuando se haga proyectos propios.

**8. Actualiza la estructura de la base de datos**
No es obligatorio pero si recomendable, por que Las migraciones actualizan la estructura de la base de datos para que coincida con los modelos definidos en tu proyecto
asegura que la base de datos esté sincronizada con tus modelos antes de iniciar el servidor de desarrollo

*python manage.py migrate*

**9. Ejecutar el servidor de desarrollo**

*python manage.py runserver*


**Estructura del proyecto**
Tu proyecto debería tener esta estructura:

text
helloworld_project/
├── helloworld/
│   ├── __init__.py       # Archivo de inicialización de Python.
│   ├── admin.py          # Configuración del panel de administración (sin cambios).
│   ├── apps.py           # Configuración de la aplicación.
│   ├── migrations/       # Migraciones para el modelo de datos.
│   ├── models.py         # Modelos de datos (sin cambios).
│   ├── tests.py          # Pruebas unitarias (sin cambios).
│   ├── urls.py           # Archivo con las rutas específicas de la aplicación.
│   └── views.py          # Archivo con las vistas (funciones que manejan solicitudes).
├── helloworld_project/
│   ├── __init__.py       # Archivo de inicialización del proyecto.
│   ├── asgi.py           # Configuración para ASGI (sin cambios).
│   ├── settings.py       # Configuración principal del proyecto.
│   ├── urls.py           # Archivo con las rutas principales del proyecto.
│   └── wsgi.py           # Configuración para WSGI (sin cambios).
└── manage.py             # Archivo para ejecutar comandos de Django.

Cuando visites http://localhost:8000/helloworld, deberías ver en tu navegador el texto: "Hello World!".

**Acabar con la conexión**

Para matar la conexion se supone que tendria que ser con Ctrl + C, pero no funciona,
entonces poner

pkill -f "python manage.py runserver"

**Comprobar si se ha cortado con la conexión**

para comprobar si hay alguno proceso pendiente. Si no hay tiene que salir en blanco.
lsof -i :8000 

si hubiera 

(django_venv) ➜  helloworld_project git:(main) ✗ lsof -i :8000

COMMAND   PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 38140 jurrutia    3u  IPv4 119460      0t0  TCP localhost:8000 (LISTEN)
python3 38140 jurrutia    4u  IPv4 124482      0t0  TCP localhost:8000->localhost:59908 (CLOSE_WAIT)
python3 38140 jurrutia    6u  IPv4 123274      0t0  TCP localhost:8000->localhost:59918 (CLOSE_WAIT)

Entonces
kill -9 38140

Y volver a comprobar con lsof -i :8000 que no sale nada
