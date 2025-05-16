# Proyecto Django: Articles (ex00 - ex06)

## Descripción
Este proyecto es una aplicación Django llamada **Articles**. Está desarrollada paso a paso siguiendo los ejercicios **ex00 a ex06**, e incluye funcionalidad como autenticación, gestión de artículos, favoritos, internacionalización, menú dinámico, permisos y una suite de tests automatizada con evidencia clara.

---

## Índice
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Desarrollo paso a paso](#desarrollo-paso-a-paso)
  - [ex00: Estructura básica y modelos](#ex00-estructura-básica-y-modelos)
  - [ex01: Listado y detalle de artículos](#ex01-listado-y-detalle-de-artículos)
  - [ex02: Autenticación y registro](#ex02-autenticación-y-registro)
  - [ex03: Favoritos y publicaciones](#ex03-favoritos-y-publicaciones)
  - [ex04: Internacionalización](#ex04-internacionalización)
  - [ex05: Menú dinámico y permisos](#ex05-menú-dinámico-y-permisos)
  - [ex06: Tests automáticos y evidencia](#ex06-tests-automáticos-y-evidencia)
- [Ejecución de los tests](#ejecución-de-los-tests)
- [Notas y buenas prácticas](#notas-y-buenas-prácticas)
- [Contacto](#contacto)

---

## Estructura del proyecto

```plaintext
articles/
    models.py
    views.py
    urls.py
    tests.py
    runner.py
    templates/
        articles/
            article_list.html
            article_detail.html
            favourites_list.html
            already_favourite.html
            favourite_added.html
            publications_list.html
            publish.html
            register.html
            login.html
    locale/
        es/
            LC_MESSAGES/
                django.po
                django.mo
        en/
            LC_MESSAGES/
                django.po
                django.mo
manage.py
settings.py
requirements.txt
README.md
```

---

## Requisitos previos

- **Python** 3.11
- **Django** 4.2.20
- **Opcional**: 
    asgiref==3.8.1
    sqlparse==0.5.3
    termcolor==3.1.0

pip install -r requirements.txt


## Desarrollo paso a paso

### ex00: Estructura básica y modelos

1. **Crear el proyecto y la app:**
   ```
   django-admin startproject myproject
   cd myproject
   python manage.py startapp articles
   ```

2. **Añadir la app a `INSTALLED_APPS` en `settings.py`:**
   ```python
   INSTALLED_APPS = [
       ...
       'articles',
   ]
   ```

3. **Definir los modelos en `articles/models.py`:**
   ```python
   from django.db import models
   from django.contrib.auth.models import User

   class Article(models.Model):
       title = models.CharField(max_length=200)
       author = models.ForeignKey(User, on_delete=models.CASCADE)
       synopsis = models.TextField()
       content = models.TextField()
       created = models.DateTimeField(auto_now_add=True)

   class UserFavouriteArticle(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       article = models.ForeignKey(Article, on_delete=models.CASCADE)

       class Meta:
           unique_together = ('user', 'article')
   ```

4. **Migrar la base de datos:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

---

### ex01: Listado y detalle de artículos

1. **Crear vistas en `articles/views.py`:**
   ```python
   from django.shortcuts import render, get_object_or_404
   from .models import Article

   def article_list(request):
       articles = Article.objects.all().order_by('-created')
       return render(request, 'articles/article_list.html', {'articles': articles})

   def article_detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       return render(request, 'articles/article_detail.html', {'article': article})
   ```

2. **Configurar URLs en `articles/urls.py`:**
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('articles/', views.article_list, name='articles'),
       path('articles/<int:pk>/', views.article_detail, name='article-detail'),
   ]
   ```

3. **Incluir las URLs de la app en el `urls.py` principal:**
   ```python
   from django.urls import include, path

   urlpatterns = [
       path('', include('articles.urls')),
       ...
   ]
   ```

4. **Crear las plantillas:**
   - **`templates/articles/article_list.html`:**
     ```html
     {% extends "base.html" %}
     {% block content %}
     <h1>Articles</h1>
     <ul>
       {% for article in articles %}
         <li>
           <a href="{% url 'article-detail' article.pk %}">{{ article.title }}</a>
         </li>
       {% endfor %}
     </ul>
     {% endblock %}
     ```

---

### ex02: Autenticación y registro

1. **Usar el sistema de usuarios de Django:**
   Añadir vistas para login (`login.html`), logout y registro (`register.html`).

2. **Ejemplo de vista de registro:**
   ```python
   from django.contrib.auth.forms import UserCreationForm
   from django.shortcuts import render, redirect

   def register(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('articles')
       else:
           form = UserCreationForm()
       return render(request, 'articles/register.html', {'form': form})
   ```

3. **Actualizar el menú en las plantillas según el usuario autenticado:**
   ```html
   {% if user.is_authenticated %}
       <a href="{% url 'logout' %}">Logout</a>
   {% else %}
       <a href="{% url 'login' %}">Login</a>
       <a href="{% url 'register' %}">Register</a>
   {% endif %}
   ```

---

### ex03: Favoritos y publicaciones
1. **Añadir vistas para favoritos y publicaciones.**
2. **Crear plantillas necesarias.**

---

### ex04: Internacionalización
1. **Configurar idiomas en `settings.py`.**
2. **Marcar textos para traducción en las plantillas.**
3. **Crear y compilar archivos de traducción.**

---

### ex05: Menú dinámico y permisos
1. **Actualizar el menú para opciones según el usuario.**
2. **Controlar permisos en vistas con `@login_required`.**

---

### ex06: Tests automáticos y evidencia
1. **Crear una suite de tests completa en `articles/tests.py`.**
2. **Añadir helper para evidencia:**
   ```python
   def print_test_details(self, description, before, action, after, passed):
       print("\n" + "=" * 60)
       print(description)
       print("ANTES:", before)
       print("ACCIÓN:", action)
       print("DESPUÉS:", after)
       print("RESULTADO:", "✅ PASÓ" if passed else "❌ FALLÓ")
       print("=" * 60)
   ```

---

## Ejecución de los tests

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar los tests:**
   ```bash
   python manage.py test articles
   ```

3. **Interpreta la salida:**
   - Cada test imprime un bloque de evidencia.
   - Si el test pasa, verás `✅ PASÓ`.
   - Si falla, verás `❌ FALLÓ` junto a la información relevante.


