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