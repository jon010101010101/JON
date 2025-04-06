from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render
from .models import Movies
import json

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
                    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                );
            """)
            cursor.execute("""
                DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies;
            """)
            cursor.execute("""
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.updated = now();
                    NEW.created = OLD.created;
                    RETURN NEW;
                END;
                $$ LANGUAGE 'plpgsql';
            """)
            cursor.execute("""
                CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def populate(request):
    data = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-05-19"},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"},
    ]

    results = []
    for entry in data:
        try:
            movie = Movies(**entry)
            movie.save()
            results.append(f"{entry['title']} inserted successfully.")
        except Exception as e:
            results.append(f"Error inserting {entry['title']}: {str(e)}")
    
    return HttpResponse("<br>".join(results))


def display(request):
    movies = Movies.objects.all()
    if not movies.exists():
        return render(request, 'ex06/display.html', {'movies': None})

    return render(request, 'ex06/display.html', {'movies': movies})


def update(request):
    if request.method == 'POST':
        title_to_update = request.POST.get('title')
        new_text = request.POST.get('opening_crawl')
        Movies.objects.filter(title=title_to_update).update(opening_crawl=new_text)

    movies = Movies.objects.all()
    if not movies.exists():
        return render(request, 'ex06/update.html', {'movies': None})

    return render(request, 'ex06/update.html', {'movies': movies})

def load_opening_crawl(request):
    try:
        # Ruta al archivo JSON
        file_path = 'ex06/data/opening_crawl.json'

        # Abrir y cargar el contenido del archivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Actualizar la base de datos con los datos del JSON
        for title, opening_crawl in data.items():
            Movies.objects.filter(title=title).update(opening_crawl=opening_crawl)

        return HttpResponse("Opening crawl data loaded successfully.")
    except FileNotFoundError:
        return HttpResponse("Error: File not found.")
    except json.JSONDecodeError:
        return HttpResponse("Error: Invalid JSON format.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
