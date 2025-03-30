from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render, redirect
from .models import Movie

# Define los datos directamente en este archivo
data = [
    {
        "title": "The Phantom Menace",
        "episode_nb": 1,
        "opening_crawl": "Turmoil has engulfed the Galactic Republic...",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "1999-05-19",
    },
    {
        "title": "Attack of the Clones",
        "episode_nb": 2,
        "opening_crawl": "There is unrest in the Galactic Senate...",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2002-05-16",
    },
    {
        "title": "Revenge of the Sith",
        "episode_nb": 3,
        "opening_crawl": "War! The Republic is crumbling under attacks...",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2005-05-19",
    },
]

# Vista para inicializar la tabla
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex06_movies (
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL,
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                END;
                $$ language 'plpgsql'
            """)
            cursor.execute("""
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column()
            """)
        return HttpResponse("Tabla ex06_movies creada correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al crear la tabla: {e}")

# Vista para poblar la tabla con datos
def populate(request):
    ok = ""
    error = ""
    for item in data:
        try:
            movie = Movie(
                title=item['title'],
                episode_nb=item['episode_nb'],
                opening_crawl=item['opening_crawl'],
                director=item['director'],
                producer=item['producer'],
                release_date=item['release_date']
            )
            movie.save()
            ok += f"Película '{item['title']}' insertada correctamente.<br>"
        except Exception as e:
            error += f"Error al insertar '{item['title']}': {e}<br>"
    if error:
        return HttpResponse(error)
    else:
        return HttpResponse(ok)

# Vista para mostrar los datos en formato HTML
def display(request):
    try:
        movies = Movie.objects.all()
        if not movies:
            return HttpResponse("No hay datos disponibles.")
        
        html = "<table border='1'><tr>"
        for field in Movie._meta.get_fields():
            html += f"<th>{field.name}</th>"
        html += "</tr>"
        
        for movie in movies:
            html += "<tr>"
            for field in Movie._meta.get_fields():
                html += f"<td>{getattr(movie, field.name)}</td>"
            html += "</tr>"
        
        html += "</table>"
        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error al mostrar los datos: {e}")

# Vista para actualizar el campo opening_crawl de una película seleccionada
def update(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        new_text = request.POST.get('opening_crawl')
        
        try:
            movie = Movie.objects.get(episode_nb=movie_id)
            movie.opening_crawl = new_text
            movie.save()
            return HttpResponse("Opening crawl actualizado correctamente.")
        except Movie.DoesNotExist:
            return HttpResponse("Error: Película no encontrada.")
    
    movies = Movie.objects.all()
    if not movies:
        return HttpResponse("No hay datos disponibles.")
    
    return render(request, 'ex06/update.html', {'movies': movies})
