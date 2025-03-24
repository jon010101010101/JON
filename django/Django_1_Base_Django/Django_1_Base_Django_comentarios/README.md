# EJERCICIO 00

**1.-Configuración del entorno:**

*Crear un entorno virtual:*

python3 -m venv venv_d05

*Activar el entorno virtual:*

source venv_d05/bin/activate

*Instalar Django:*

pip install django

**2.-Crear el proyecto Django:**

django-admin startproject d05

**3.-Crear la aplicación ex00:**

cd d05
python3 manage.py startapp ex00

**4.-Configurar el proyecto:**

Editar d05/settings.py:

Añadir 'ex00' a INSTALLED_APPS







**5.-Crear la vista:**

*Editar ex00/views.py:*

from django.shortcuts import render

def markdown_cheatsheet(request):
    return render(request, 'ex00/index.html')


**6.-Configurar las URLs:**

*Crear ex00/urls.py:*

from django.urls import path
from . import views

urlpatterns = [
    path('', views.markdown_cheatsheet, name='markdown_cheatsheet'),
]

*Editar d05/urls.py:*

from django.urls import path, include

urlpatterns = [
    path('ex00/', include('ex00.urls')),
]

**7.-Crear la plantilla HTML:**

*Crear el directorio:*

mkdir -p ex00/templates/ex00

Crear ex00/templates/ex00/index.html con el contenido de la cheatsheet de Markdown

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Cheatsheet</title>
</head>
<body>
    <h1>Markdown Cheatsheet</h1>

    <h2>Headers</h2>
    <p># H1<br>## H2<br>### H3</p>

    <h2>Emphasis</h2>
    <p>*italic*<br>**bold**<br>***bold italic***</p>

    <h2>Lists</h2>
    <p>
        Unordered:<br>
        * Item 1<br>
        * Item 2<br>
        Ordered:<br>
        1. First item<br>
        2. Second item
    </p>

    <h2>Links</h2>
    <p>[Link text](URL)</p>

    <h2>Images</h2>
    <p>![Alt text](URL)</p>

    <h2>Code</h2>
    <p>`Inline code`<br><br>Code block:<br>```
function example() {
  console.log("Hello, World!");
}
```</p>

    <h2>Blockquotes</h2>
    <p>> This is a blockquote</p>

    <h2>Horizontal Rule</h2>
    <p>---</p>
</body>
</html>



```
esto aqui es para que se quite lo creado por el markdown
**8.-Ejecutar el servidor:**

Desde la carpeta que contenga manage.py
(venv_d05) ➜  d05 git:(main) ✗ ls
d05  ex00  manage.py


python3 manage.py runserver

**Verificar la aplicación:**

Abrir un navegador y visitar http://localhost:8000/ex00/

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

# EJERCICIO 01


Crea la aplicación ex01:

bash
python manage.py startapp ex01
Estructura de archivos del proyecto:

text
project_root/
│
├── manage.py
├── requirements.txt
├── project_name/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ex01/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── ex01/
│       │   ├── base.html
│       │   ├── nav.html
│       │   ├── django.html
│       │   ├── display.html
│       │   └── templates.html
│
├── static/
│   ├── css/
│   │   ├── style1.css
│   │   └── style2.css
│
└── staticfiles/
Configura las URLs:

En project_name/urls.py:

python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex01/', include('ex01.urls')),
]
En ex01/urls.py:

python
from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_view, name='django'),
    path('display/', views.display_view, name='display'),
    path('templates/', views.templates_view, name='templates'),
]
Crea las vistas en ex01/views.py:

python
from django.shortcuts import render

def django_view(request):
    return render(request, 'ex01/django.html')

def display_view(request):
    return render(request, 'ex01/display.html')

def templates_view(request):
    return render(request, 'ex01/templates.html')
Crea los templates:

ex01/templates/ex01/base.html:

xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
    {% block style %}
    <link rel="stylesheet" href="{% static 'css/style1.css' %}">
    {% endblock %}
</head>
<body>
    {% include 'ex01/nav.html' %}
    {% block content %}{% endblock %}
</body>
</html>
ex01/templates/ex01/nav.html:

xml
<nav>
    <ul>
        <li><a href="{% url 'django' %}">Django</a></li>
        <li><a href="{% url 'display' %}">Display Process</a></li>
        <li><a href="{% url 'templates' %}">Template Engine</a></li>
    </ul>
</nav>
Crea los templates django.html, display.html, y templates.html extendiendo de base.html y llenando el contenido apropiado para cada página.

Crea los archivos CSS:

static/css/style1.css:

css
body {
    color: blue;
}
static/css/style2.css:

css
body {
    color: red;
}
Configura los archivos estáticos en settings.py:

python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
Ejecuta collectstatic:

bash
python manage.py collectstatic
Actualiza requirements.txt:

bash
pip freeze > requirements.txt









# EJERCICIO 02

**1.-Crear el Proyecto Django**

Activar el entorno virtual Django

Crear un nuevo proyecto: django-admin startproject config . en el directorio ex02

**2.-Crear la Aplicación**

Crear una nueva aplicación: python manage.py startapp ex02

**3.-Configurar settings.py**

Editar config/settings.py:

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE_PATH = os.path.join(BASE_DIR, 'ex02', 'logs.txt')

INSTALLED_APPS = [
    # ... otras apps ...
    'ex02.apps.Ex02Config',
]
**4.-Crear Modelos y Formularios**

*Crear ex02/models.py:*

from django.db import models

class LogEntry(models.Model):
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: {self.text}"

*Crear ex02/forms.py:*

from django import forms

class LogForm(forms.Form):
    text = forms.CharField(max_length=255)

**5.-Implementar Vistas**

*Editar ex02/views.py:*

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LogForm
from .models import LogEntry
from datetime import datetime

def ex02_view(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            LogEntry.objects.create(text=text)
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp}: {text}\n"
            
            with open(settings.LOG_FILE_PATH, 'a') as log_file:
                log_file.write(log_entry)
            
            return redirect('ex02')
    else:
        form = LogForm()
    
    logs = LogEntry.objects.all().order_by('-timestamp')
    return render(request, 'ex02/index.html', {'form': form, 'logs': logs})

**6. Crear Plantillas**

*Crear ex02/templates/ex02/index.html:*

xml
<!DOCTYPE html>
<html>
<head>
    <title>Ex02</title>
</head>
<body>
    <h1>Ex02</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>

    <h2>History</h2>
    <ul>
        {% for log in logs %}
            <li>{{ log.timestamp|date:"Y-m-d H:i:s" }}: {{ log.text }}</li>
        {% endfor %}
    </ul>
</body>
</html>

**7.-Configurar URLs**

*Editar config/urls.py:*

from django.contrib import admin
from django.urls import path
from ex02.views import ex02_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex02/', ex02_view, name='ex02'),
]

**8.-Realizar Migraciones**

*Ejecutar:*

python manage.py makemigrations
python manage.py migrate

**9.-Ejecutar el Servidor**

Iniciar el servidor: python manage.py runserver

**10.-Verificar Funcionalidad**

Acceder a http://localhost:8000/ex03/

Probar el formulario y verificar el historial

**11.-Crear requirements.txt**

Ejecutar: pip freeze > requirements.txt o mejor meterlos a mano

**12.-Verificar logs.txt**

Revisar el contenido de ex02/logs.txt

# Archivos modificados y creados:

config/settings.py: Configuración del proyecto

config/urls.py: Configuración de URLs

ex02/models.py: Definición del modelo LogEntry

ex02/forms.py: Definición del formulario LogForm

ex02/views.py: Implementación de la vista ex02_view

ex02/templates/ex02/index.html: Plantilla HTML

requirements.txt: Lista de dependencias del proyecto

ex02/logs.txt: Archivo de logs (creado automáticamente)


**Para desconectar el servidor**

*Ctrl + z para suspender*

*pkill -f "python manage.py runserver"*
*lsof -i :8000*
*kill -9 38140 (el numero depende del que salga del punto anterior)*


*Para limpiar por si aveces los archivos compilados causan problemas*
find . -name "*.pyc" -delete




# EJERCICIO 03


**Crear un entorno virtual e instalarlo:**

python3 -m venv env
source env/bin/activate


**Instalar Django en el entorno virtual:**

pip install django

Luego, para crear el nuevo proyecto Django y la aplicación:

**Crear el proyecto Django:**

django-admin startproject color_table .

**Crear la aplicación 'table_app' dentro del proyecto:**

python manage.py startapp table_app

**Registrar la nueva aplicación en INSTALLED_APPS en el archivo settings.py del proyecto:**

INSTALLED_APPS = [
    ...
    'table_app.apps.TableAppConfig',
]

**Configurar las URLs del proyecto para incluir las de la aplicación, editando el archivo urls.py del proyecto:**

from django.urls import path, include

urlpatterns = [
    ...
    path('', include('table_app.urls')),
]

**Crear un archivo urls.py en la carpeta de la aplicación table_app para definir las rutas específicas.**


**Crear una nueva aplicación dentro del proyecto (llamada 'table_app' o similar)**

*Estructura del proyecto*

proyecto_django/
├── manage.py
├── proyecto_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── table_app/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    └── templates/
        └── table_app/
            └── color_table.html

**Configuración de la aplicación**

Añadir 'table_app' a INSTALLED_APPS en settings.py

**Creación de la vista (views.py)**

Importar render de django.shortcuts

**Crear la función color_table:**

from django.shortcuts import render

def color_table(request):
    colors = ['noir', 'rouge', 'bleu', 'vert']
    rows = []
    for i in range(50):
        row = []
        for color in colors:
            if color == 'noir':
                shade = f'#{i*5:02x}{i*5:02x}{i*5:02x}'
            elif color == 'rouge':
                shade = f'#{i*5:02x}0000'
            elif color == 'bleu':
                shade = f'#0000{i*5:02x}'
            else:  # vert
                shade = f'#00{i*5:02x}00'
            row.append(shade)
        rows.append(row)

    context = {
        'colors': colors,
        'rows': rows,
    }
    return render(request, 'table_app/color_table.html', context)

**Creación de la plantilla HTML (color_table.html)**

<!DOCTYPE html>
<html>
<head>
    <title>Color Table</title>
    <style>
        table {
            border-collapse: collapse;
        }
        td {
            width: 80px;
            height: 40px;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            {% for color in colors %}
                <th>{{ color }}</th>
            {% endfor %}
        </tr>
        {% for row in rows %}
            <tr>
                {% for shade in row %}
                    <td style="background-color: {{ shade }};"></td>
                {% endfor %}
            </tr>
        {% endfor %}
    </table>
</body>
</html>

**Configuración de URLs**

En urls.py del proyecto, incluir la URL de la aplicación

*Crear urls.py en la aplicación table_app si no existe*

from django.urls import path
from . import views

urlpatterns = [
    path('', views.color_table, name='color_table'),
]

*Configurar la URL para la vista color_table*

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Incluye las URLs de 'myapp'
    # Añade más inclusiones de aplicaciones si es necesario
]


**Depuración y ajustes**

Corregir errores de sintaxis en la plantilla

Ajustar la generación de colores para usar códigos hexadecimales

Asegurar que la función render esté importada correctamente

**Pruebas y verificación**

Ejecutar el servidor de desarrollo (python manage.py runserver)

Acceder a la URL de la tabla de colores en el navegador

Verificar que la tabla se muestre correctamente con los degradados de colores

**Optimización y mejoras finales**

Ajustar estilos CSS si es necesario

Asegurar que el código siga las mejores prácticas de Django


# Ejeccucion


python manage.py makemigrations
python manage.py makemigrations

chrome://settings/clearBrowserData (para limpiar caché)

python manage.py runserver
http://localhost:8000/ex03/



# Para cortar conexion
Ctrl + Z
pkill -f "python manage.py runserver"
lsof -i :8000
kill -9 38140