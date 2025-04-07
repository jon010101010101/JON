from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie  # Importa el modelo Movie
from django.db import IntegrityError
import json
import os

def populate(request):
    movies_data = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-05-19"},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"},
    ]

    try:
        # Eliminar las entradas existentes para evitar duplicados
        Movie.objects.all().delete()

        for movie_data in movies_data:
            try:
                # Crear una instancia de Movie con los datos
                movie = Movie(**movie_data)
                movie.save()  # Guardar la instancia en la base de datos
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")  # Devuelve un mensaje de error en caso de fallo
        return HttpResponse("OK")  # Devuelve "OK" en caso de éxito
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    movies = Movie.objects.all()  # Utiliza Movie en lugar de Movies
    if not movies:
        return HttpResponse("No data available")
    return render(request, 'ex07/display.html', {'movies': movies})

def update(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        opening_crawl = request.POST.get('opening_crawl')
        try:
            movie = Movie.objects.get(pk=movie_id)
            movie.opening_crawl = opening_crawl
            movie.save()
            return HttpResponse(f"OK: Movie '{movie.title}' updated successfully.")
        except Movie.DoesNotExist:
            return HttpResponse("Error: No movie found with the selected ID.")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    else:
        movies = Movie.objects.all()
        if not movies:
            return HttpResponse("No data available")
        return render(request, 'ex07/update.html', {'movies': movies})

def load_opening_crawl(request):
    try:
        # Ruta al archivo JSON
        file_path = os.path.join(os.getcwd(), 'data', 'opening_crawl.json')  # Ruta absoluta al archivo

        # Abrir y cargar el contenido del archivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Actualizar la base de datos con los datos del JSON
        for title, opening_crawl in data.items():
            try:
                movie = Movie.objects.get(title=title)
                movie.opening_crawl = opening_crawl
                movie.save()
            except Movie.DoesNotExist:
                return HttpResponse(f"Error: Movie with title '{title}' does not exist.")
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")

        return HttpResponse("Opening crawl data loaded successfully.")
    except FileNotFoundError:
        return HttpResponse("Error: File not found.")
    except json.JSONDecodeError:
        return HttpResponse("Error: Invalid JSON format.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")