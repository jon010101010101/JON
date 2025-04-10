from django.shortcuts import render, HttpResponse
from .models import Movies
from datetime import date

def populate(request):
    data = [
        {'episode_nb': 1, 'title': "The Phantom Menace", 'director': "George Lucas", 'producer': "Rick McCallum", 'release_date': date(1999, 5, 19)},
        {'episode_nb': 2, 'title': "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", 'release_date': date(2002, 5, 16)},
        {'episode_nb': 3, 'title': "Revenge of the Sith", 'director': "George Lucas", 'producer': "Rick McCallum", 'release_date': date(2005, 5, 19)},
        {'episode_nb': 4, 'title': "A New Hope", 'director': "George Lucas", 'producer': "Gary Kurtz, Rick McCallum", 'release_date': date(1977, 5, 25)},
        {'episode_nb': 5, 'title': "The Empire Strikes Back", 'director': "Irvin Kershner", 'producer': "Gary Kurtz, Rick McCallum", 'release_date': date(1980, 5, 17)},
        {'episode_nb': 6, 'title': "Return of the Jedi", 'director': "Richard Marquand", 'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum", 'release_date': date(1983, 5, 25)},
        {'episode_nb': 7, 'title': "The Force Awakens", 'director': "J. J. Abrams", 'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk", 'release_date': date(2015, 12, 11)},
    ]

    try:
        Movies.objects.all().delete()  # Elimina las entradas existentes

        for movie_data in data:
            movie = Movies(**movie_data)
            movie.save()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available")

        return render(request, 'ex03/display.html', {'movies': movies})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
