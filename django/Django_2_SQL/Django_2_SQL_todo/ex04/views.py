import psycopg2
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex04_movies (
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INTEGER PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM ex04_movies;")
            for episode_nb, title, director, producer, release_date in data:
                cursor.execute(
                    "INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date) VALUES (%s, %s, %s, %s, %s)",
                    (episode_nb, title, director, producer, release_date),
                )
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT episode_nb, title, director, producer, release_date FROM ex04_movies;")
            movies = cursor.fetchall()

            if movies:
                return render(request, 'ex04/display.html', {'movies': movies})
            else:
                return HttpResponse("No data available")
    except Exception:
        return HttpResponse("No data available")

@csrf_exempt
def remove(request):
    try:
        with connection.cursor() as cursor:
            message = ""

            if request.method == 'POST':
                title_to_remove = request.POST.get('title')
                cursor.execute("DELETE FROM ex04_movies WHERE title = %s;", [title_to_remove])
                connection.commit()
                message = f"{title_to_remove} removed successfully."

            cursor.execute("SELECT title FROM ex04_movies;")
            titles = [row[0] for row in cursor.fetchall()]

            if not titles:
                return HttpResponse("No data available")

            return render(request, 'ex04/remove.html', {'titles': titles, 'message': message})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
