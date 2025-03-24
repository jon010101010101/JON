"""
Al crearlo se crea automaticamnete ne ingles

Configuración de URLs para el proyecto d05.

La lista `urlpatterns` dirige las URLs a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Ejemplos:
Vistas basadas en funciones
    1. Añade una importación:  from mi_app import views  # Importa el módulo 'views' de tu aplicación 'mi_app'
    2. Añade una URL a urlpatterns:  path('', views.home, name='home')  # Define una ruta para la página de inicio ('') que llama a la función 'home' en 'views' y le asigna el nombre 'home'

Vistas basadas en clases
    1. Añade una importación:  from otra_app.views import Home  # Importa la clase 'Home' del módulo 'views' en la aplicación 'otra_app'
    2. Añade una URL a urlpatterns:  path('', Home.as_view(), name='home')  # Define una ruta para la página de inicio que llama al método 'as_view()' de la clase 'Home' y le asigna el nombre 'home'

Incluyendo otra URLconf (configuración de URLs)
    1. Importa la función include(): from django.urls import include, path  # Importa 'include' y 'path' de 'django.urls'
    2. Añade una URL a urlpatterns:  path('blog/', include('blog.urls'))  # Incluye las URLs definidas en el archivo 'urls.py' de la aplicación 'blog' para cualquier ruta que comience con 'blog/'
"""

from django.urls import path, include  # Importa las funciones necesarias para 
# definir rutas (path) y para incluir rutas de otras aplicaciones (include)

urlpatterns = [
    # Define una ruta que comienza con 'ex00/'
    # Cuando un usuario accede a una URL que empieza con 'ex00/', Django buscará 
    # las rutas definidas en el archivo 'urls.py' de la aplicación 'ex00'
    path('ex00/', include('ex00.urls')),
]
