from django.shortcuts import render, HttpResponse
from django.db import connections

def init(request):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex02_movies (
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
        return HttpResponse(f"Error: {e}")

def populate(request):
    try:
        with connections['default'].cursor() as cursor:
            # Verificar si la tabla está vacía
            cursor.execute("SELECT COUNT(*) FROM ex02_movies")
            count = cursor.fetchone()[0]

            if count == 0:
                movies = [
                    (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
                    (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
                    (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
                    (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
                    (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
                    (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
                    (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
                ]
                for movie in movies:
                    cursor.execute("""
                        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s)
                    """, movie)
                return HttpResponse("OK")
            else:
                return HttpResponse("Data already exists")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def display(request):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM ex02_movies")
            movies = cursor.fetchall()
            if not movies:
                return HttpResponse("No data available")
            html = "<table><tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
            for movie in movies:
                html += f"<tr><td>{movie[0]}</td><td>{movie[1]}</td><td>{movie[2]}</td><td>{movie[3]}</td><td>{movie[4]}</td></tr>"
            html += "</table>"
            return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {e}")
