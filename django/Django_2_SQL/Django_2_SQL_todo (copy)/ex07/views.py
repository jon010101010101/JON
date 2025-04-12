from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie
from django.conf import settings
import os
import json


def populate(request):
    # Ruta al archivo JSON
    json_file_path = os.path.join(settings.BASE_DIR, 'data', 'opening_crawl.json')

    # Verificar si el archivo existe
    if not os.path.exists(json_file_path):
        return HttpResponse(f"Error: JSON file not found at {json_file_path}")

    try:
        # Leer el archivo JSON
        with open(json_file_path, 'r') as file:
            movies_data = json.load(file)

        # Detalles adicionales de las películas (sin opening_crawl)
        movie_details = {
    "The Phantom Menace": {
        "episode_nb": 1,
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "1999-05-19"
    },
    "Attack of the Clones": {
        "episode_nb": 2,
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2002-05-16"
    },
    "Revenge of the Sith": {
        "episode_nb": 3,
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2005-05-19"
    },
    "A New Hope": {
        "episode_nb": 4,
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25"
    },
    "The Empire Strikes Back": {
        "episode_nb": 5,
        "director": "Irvin Kershner",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1980-05-17"
    },
    "Return of the Jedi": {
        "episode_nb": 6,
        "director": "Richard Marquand",
        "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
        "release_date": "1983-05-25"
    },
    "The Force Awakens": {
        "episode_nb": 7,
        "director": "J. J. Abrams",
        "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
        "release_date": "2015-12-18"
    }
}
        # Insertar o actualizar registros en la base de datos
        for title, opening_crawl in movies_data.items():
            if title in movie_details:
                details = movie_details[title]
                Movie.objects.update_or_create(
                    episode_nb=details["episode_nb"],
                    defaults={
                        'title': title,
                        'director': details["director"],
                        'producer': details["producer"],
                        'release_date': details["release_date"],
                        'opening_crawl': opening_crawl
                    }
                )

        return HttpResponse("OK")  # Mostrar solo OK si todo se ejecuta correctamente

    except json.JSONDecodeError as e:
        return HttpResponse(f"Error: JSON file is not properly formatted. {e}")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def display(request):
    try:
        # Obtener todas las películas ordenadas por episode_nb
        movies = Movie.objects.all().order_by('episode_nb')
        if not movies.exists():  # Si no hay películas disponibles
            return HttpResponse("No data available")
        
        return render(request, 'ex07/display.html', {'movies': movies})  # Renderizar el template con los datos
    
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def update(request):
    message = None  # Inicializar el mensaje

    if request.method == 'POST':
        # Obtener el episode_nb y el nuevo opening_crawl del formulario
        episode_nb = request.POST.get('movie')  # Cambiar 'episode_nb' a 'movie'
        opening_crawl = request.POST.get('opening_crawl')

        # Verificar que episode_nb no sea None ni vacío
        if episode_nb:
            try:
                # Obtener la película o devolver un error 404 si no existe
                movie = get_object_or_404(Movie, episode_nb=episode_nb)

                # Actualizar el campo opening_crawl de la película
                movie.opening_crawl = opening_crawl
                movie.save()

                message = "Update successful!"  # Mensaje de éxito
            except Exception as e:
                message = f"Error updating movie: {e}"  # Mensaje de error
        else:
            message = "Error: episode_nb is missing"  # Mensaje de error

    # Si la solicitud no es POST, obtener todas las películas y renderizar el template con las películas
    movies = Movie.objects.all()
    return render(request, 'ex07/update.html', {'movies': movies, 'message': message})