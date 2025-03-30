from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

def populate(request):
    data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        # Agrega más entradas de datos aquí según sea necesario
    ]

    response = ""
    for entry in data:
        try:
            movie = Movie(**entry)
            movie.save()
            response += f"OK: {entry['title']}<br>"
        except Exception as e:
            response += f"Error: {str(e)}<br>"

    return HttpResponse(response)

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
            return HttpResponse("OK")
        except Movie.DoesNotExist:
            return HttpResponse("No data available")
    else:
        movies = Movie.objects.all()
        if not movies:
            return HttpResponse("No data available")
        return render(request, 'ex07/update.html', {'movies': movies})