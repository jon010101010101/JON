# Proyecto Django: Ejercicios ex00 - ex05

Este proyecto es una serie de ejercicios diseñados para introducir a los desarrolladores en el desarrollo web con Django. Cada ejercicio se centra en un aspecto específico del framework, desde la creación de modelos simples hasta la implementación de formularios y la interacción con bases de datos.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

Django_2_SQL/
├── d42/ # Directorio principal del proyecto Django
│ ├── asgi.py
│ ├── init.py
│ ├── pycache/
│ ├── settings.py # Configuración del proyecto
│ ├── urls.py # Definición de las URLs del proyecto
│ └── wsgi.py
├── ex00/ # Aplicación Django para el ejercicio 00
│ ├── admin.py
│ ├── apps.py
│ ├── init.py
│ ├── migrations/
│ ├── models.py
│ ├── pycache/
│ ├── tests.py
│ ├── urls.py # Definición de las URLs de la aplicación
│ └── views.py # Definición de las vistas de la aplicación
├── ex01/ # Aplicación Django para el ejercicio 01
│ └── ... # Estructura similar a ex00/
├── ex02/ # Aplicación Django para el ejercicio 02
│ └── ... # Estructura similar a ex00/
├── ex03/ # Aplicación Django para el ejercicio 03
│ └── ... # Estructura similar a ex00/
├── ex04/ # Aplicación Django para el ejercicio 04
│ └── ... # Estructura similar a ex00/
├── ex05/ # Aplicación Django para el ejercicio 05
│ └── ... # Estructura similar a ex00/
├── db.sqlite3 # Base de datos SQLite
├── docker-compose.yml # Configuración de Docker Compose
├── Dockerfile # Definición de la imagen Docker
├── manage.py # Script para administrar el proyecto Django
└── requirements.txt # Lista de dependencias de Python


## Configuración de Docker

Para ejecutar el proyecto con Docker, sigue estos pasos:

1.  **Crea el archivo `Dockerfile`:**

    ```
    FROM python:3.10

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    ```

2.  **Crea el archivo `docker-compose.yml`:**

    ```
    version: "3.9"
    services:
      web:
        build: .
        ports:
          - "8000:8000"
        volumes:
          - .:/app
        depends_on:
          - db
      db:
        image: postgres:13
        volumes:
          - postgres_data:/var/lib/postgresql/data/
        environment:
          - POSTGRES_USER=django
          - POSTGRES_PASSWORD=django
          - POSTGRES_DB=django

    volumes:
      postgres_data:
    ```

3.  **Ejecuta los siguientes comandos:**

    ```
    docker-compose build
    docker-compose up -d
    ```

## Ejercicios (ex00 - ex05)

A continuación, se presenta un resumen detallado de cada ejercicio, incluyendo los archivos que se crearon o modificaron, y los comandos que se ejecutaron:

### ex00 - "Hello, Django!"

*   **Objetivo:** Configurar un entorno de desarrollo básico con Django y mostrar un mensaje simple en el navegador.
*   **Pasos:**
    1.  **Creación del proyecto Django:**

        ```
        django-admin startproject d42
        cd d42
        python manage.py startapp ex00
        ```

    2.  **Modificación del archivo `d42/settings.py`:**

        *   Agrega `ex00` a la lista `INSTALLED_APPS`:

            ```
            INSTALLED_APPS = [
                ...
                'ex00',
            ]
            ```

    3.  **Creación del archivo `ex00/views.py`:**

        ```
        from django.http import HttpResponse

        def index(request):
            return HttpResponse("Hello, Django!")
        ```

    4.  **Creación del archivo `ex00/urls.py`:**

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        ```

    5.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('ex00.urls')),
        ]
        ```

    6.  **Ejecución del servidor de desarrollo:**

        ```
        python manage.py runserver
        ```

### ex01 - "Models"

*   **Objetivo:** Crear un modelo de datos simple y mostrar información en una plantilla HTML.
*   **Pasos:**
    1.  **Creación del modelo en `ex01/models.py`:**

        ```
        from django.db import models

        class Persona(models.Model):
            nombre = models.CharField(max_length=50)
            apellido = models.CharField(max_length=50)
            edad = models.IntegerField()

            def __str__(self):
                return f"{self.nombre} {self.apellido}"
        ```

    2.  **Creación de la migración:**

        ```
        python manage.py makemigrations ex01
        python manage.py migrate
        ```

    3.  **Creación de la vista en `ex01/views.py`:**

        ```
        from django.shortcuts import render
        from .models import Persona

        def index(request):
            personas = Persona.objects.all()
            return render(request, 'ex01/index.html', {'personas': personas})
        ```

    4.  **Creación de la plantilla `ex01/templates/ex01/index.html`:**

        ```
        <!DOCTYPE html>
        <html>
        <head>
            <title>Lista de Personas</title>
        </head>
        <body>
            <h1>Lista de Personas</h1>
            <ul>
                {% for persona in personas %}
                    <li>{{ persona.nombre }} {{ persona.apellido }} ({{ persona.edad }})</li>
                {% endfor %}
            </ul>
        </body>
        </html>
        ```

    5.  **Modificación del archivo `ex01/urls.py`:**

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        ```

    6.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('ex01/', include('ex01.urls')),
        ]
        ```

### ex02 - "Forms"

*   **Objetivo:** Crear un formulario para permitir a los usuarios ingresar datos y guardarlos en la base de datos.
*   **Pasos:**
    1.  **Creación del formulario en `ex02/forms.py`:**

        ```
        from django import forms
        from .models import Persona

        class PersonaForm(forms.ModelForm):
            class Meta:
                model = Persona
                fields = ['nombre', 'apellido', 'edad']
        ```

    2.  **Modificación de la vista en `ex02/views.py`:**

        ```
        from django.shortcuts import render, redirect
        from .forms import PersonaForm

        def index(request):
            if request.method == 'POST':
                form = PersonaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('index')
            else:
                form = PersonaForm()
            return render(request, 'ex02/index.html', {'form': form})
        ```

    3.  **Creación de la plantilla `ex02/templates/ex02/index.html`:**

        ```
        <!DOCTYPE html>
        <html>
        <head>
            <title>Formulario de Persona</title>
        </head>
        <body>
            <h1>Formulario de Persona</h1>
            <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Guardar</button>
            </form>
        </body>
        </html>
        ```

    4.  **Modificación del archivo `ex02/urls.py`:**

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        ```

    5.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('ex02/', include('ex02.urls')),
        ]
        ```

### ex03 - "Database"

*   **Objetivo:** Interactuar con la base de datos para mostrar, agregar, modificar y eliminar registros.
*   **Pasos:**
    1.  **Creación de vistas para listar, crear, actualizar y eliminar registros en `ex03/views.py`:**

        ```
        from django.shortcuts import render, redirect, get_object_or_404
        from .models import Persona
        from .forms import PersonaForm

        def listar_personas(request):
            personas = Persona.objects.all()
            return render(request, 'ex03/listar_personas.html', {'personas': personas})

        def crear_persona(request):
            if request.method == 'POST':
                form = PersonaForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('listar_personas')
            else:
                form = PersonaForm()
            return render(request, 'ex03/crear_persona.html', {'form': form})

        def editar_persona(request):
            persona = get_object_or_404(Persona, pk=id)
            if request.method == 'POST':
                form = PersonaForm(request.POST, instance=persona)
                if form.is_valid():
                    form.save()
                    return redirect('listar_personas')
            else:
                form = PersonaForm(instance=persona)
            return render(request, 'ex03/editar_persona.html', {'form': form})

        def eliminar_persona(request, id):
            persona = get_object_or_404(Persona, pk=id)
            persona.delete()
            return redirect('listar_personas')
        ```

    2.  **Creación de las plantillas HTML en `ex03/templates/ex03/`:**

        *   `listar_personas.html`
        *   `crear_persona.html`
        *   `editar_persona.html`

    3.  **Modificación del archivo `ex03/urls.py`:**

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.listar_personas, name='listar_personas'),
            path('crear/', views.crear_persona, name='crear_persona'),
            path('editar/<int:id>/', views.editar_persona, name='editar_persona'),
            path('eliminar/<int:id>/', views.eliminar_persona, name='eliminar_persona'),
        ]
        ```

    4.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('ex03/', include('ex03.urls')),
        ]
        ```

### ex04 - "Generic Views"

*   **Objetivo:** Utilizar las vistas genéricas de Django para simplificar el código y reducir la cantidad de código repetitivo.
*   **Pasos:**
    1.  **Reemplazo de las vistas basadas en funciones por vistas genéricas en `ex04/views.py`:**

        ```
        from django.views.generic import ListView, CreateView, UpdateView, DeleteView
        from django.urls import reverse_lazy
        from .models import Persona

        class PersonaListView(ListView):
            model = Persona
            template_name = 'ex04/listar_personas.html'

        class PersonaCreateView(CreateView):
            model = Persona
            form_class = PersonaForm
            template_name = 'ex04/crear_persona.html'
            success_url = reverse_lazy('ex04:listar_personas')

        class PersonaUpdateView(UpdateView):
            model = Persona
            form_class = PersonaForm
            template_name = 'ex04/editar_persona.html'
            success_url = reverse_lazy('ex04:listar_personas')

        class PersonaDeleteView(DeleteView):
            model = Persona
            template_name = 'ex04/eliminar_persona.html'
            success_url = reverse_lazy('ex04:listar_personas')
        ```

    2.  **Creación de las plantillas HTML en `ex04/templates/ex04/`:**

        *   `listar_personas.html`
        *   `crear_persona.html`
        *   `editar_persona.html`
        *   `eliminar_persona.html`

    3.  **Modificación del archivo `ex04/urls.py`:**

        ```
        from django.urls import path
        from . import views

        app_name = 'ex04'

        urlpatterns = [
            path('', views.PersonaListView.as_view(), name='listar_personas'),
            path('crear/', views.PersonaCreateView.as_view(), name='crear_persona'),
            path('editar/<int:pk>/', views.PersonaUpdateView.as_view(), name='editar_persona'),
            path('eliminar/<int:pk>/', views.PersonaDeleteView.as_view(), name='eliminar_persona'),
        ]
        ```

    4.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('ex04/', include('ex04.urls')),
        ]
        ```

### ex05 - "Templates"

*   **Objetivo:** Aprender a usar los templates de Django, a pasar variables del "backend" al "frontend" y a usar estructuras de control.
*   **Pasos:**

    1.  **Modificación de la vista en `ex05/views.py`:**

        ```
        from django.shortcuts import render
        from .models import Persona

        def index(request):
            personas = Persona.objects.all()
            context = {'personas': personas, 'mensaje': '¡Hola desde el backend!'}
            return render(request, 'ex05/index.html', context)
        ```

    2.  **Creación de la plantilla `ex05/templates/ex05/index.html`:**

        ```
        <!DOCTYPE html>
        <html>
        <head>
            <title>Ejemplo de Templates</title>
        </head>
        <body>
            <h1>Lista de Personas</h1>
            <ul>
                {% for persona in personas %}
                    <li>{{ persona.nombre }} {{ persona.apellido }} ({{ persona.edad }})</li>
                {% endfor %}
            </ul>
            <p>{{ mensaje }}</p>
        </body>
        </html>
        ```

    3.  **Modificación del archivo `ex05/urls.py`:**

        ```
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        ```

    4.  **Modificación del archivo `d42/urls.py`:**

        ```
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('ex05/', include('ex05.urls')),
        ]
        ```





find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
