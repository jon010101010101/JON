from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from django.db import IntegrityError
from datetime import date
from django.views.decorators.csrf import csrf_exempt # Eliminar esta línea

def populate(request):
    """
    Inserta datos de películas en la base de datos usando el ORM de Django.
    Inserts movie data into the database using Django's ORM.
    """
    data = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(1999, 5, 19)},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2002, 5, 16)},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2005, 5, 19)},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1977, 5, 25)},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1980, 5, 17)},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": date(1983, 5, 25)},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": date(2015, 12, 11)},
    ]

    for entry in data:
        try:
            movie, created = Movies.objects.update_or_create(
                episode_nb=entry["episode_nb"],
                defaults={
                    'title': entry["title"],
                    'director': entry["director"],
                    'producer': entry["producer"],
                    'release_date': entry["release_date"]
                }
            )
            if created:
                print(f"{entry['title']} inserted successfully.")
            else:
                print(f"{entry['title']} updated successfully.")
        except IntegrityError as e:
            print(f"Error inserting {entry['title']}: {e}")
    return HttpResponse("OK")

def display(request):
    """
    Muestra todas las películas en una tabla HTML.
    Displays all movies in an HTML table.
    """
    movies = Movies.objects.all()
    return render(request, 'ex05/display.html', {'movies': movies})

def remove(request):
    """
    Muestra un formulario para eliminar películas y maneja la eliminación.
    Displays a form to remove movies and handles the deletion.
    """
    message = None
    if request.method == 'POST':
        title_to_remove = request.POST.get('title')
        try:
            movie = Movies.objects.get(title=title_to_remove)
            movie.delete()
            message = f"Movie '{title_to_remove}' deleted successfully."
        except Movies.DoesNotExist:
            message = f"Movie '{title_to_remove}' not found."

    movies = Movies.objects.all()
    return render(request, 'ex05/remove.html', {'movies': movies, 'message': message})



# Al eliminar la decoración @csrf_exempt (la tenia en remove) de la vista remove, estás permitiendo 
# que Django aplique su protección CSRF por defecto.