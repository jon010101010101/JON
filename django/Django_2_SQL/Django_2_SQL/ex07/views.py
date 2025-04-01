from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.db import IntegrityError
from .models import Planet, Person 

def populate(request):
    data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        },
    ]

    response = ""
    for entry in data:
        try:
            movie = Movie(**entry)  # Crea una instancia de Movie
            movie.save()  # Guarda la película en la base de datos
            response += f"OK: {entry['title']}<br>"  # Mensaje de éxito
        except IntegrityError:
            response += f"Error: Duplicate entry for {entry['title']}<br>"  # Manejo de duplicados
        except Exception as e:
            response += f"Error: {str(e)}<br>"  # Manejo de otros errores

    return HttpResponse(response)  # Devuelve la respuesta

def display(request):
    movies = Movie.objects.all()
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