from django.http import HttpResponse
import psycopg2
from django.shortcuts import render
from django.conf import settings

def get_db_connection():
    return psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

# Vista para crear la tabla
def init(request):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies (
                episode_nb INT PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vista para insertar datos en la tabla
def populate(request):
    data = [
        (1, "The Phantom Menace", "A long time ago in a galaxy far, far away...", "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", "There is unrest in the Galactic Senate...", "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", "War! The Republic is crumbling...", "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", "It is a period of civil war...", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", "It is a dark time for the Rebellion...", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Luke Skywalker has returned to his home planet...", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "Luke Skywalker has vanished...", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM ex02_movies;")
        for episode_nb, title, opening_crawl, director, producer, release_date in data:
            try:
                cur.execute("""
                    INSERT INTO ex02_movies (episode_nb, title, opening_crawl, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (episode_nb, title, opening_crawl, director, producer, release_date))
                conn.commit()
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}") # Returns error if any insertion fails

        cur.close()
        conn.close()
        return HttpResponse("OK") # If all insertions succeed, return OK
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vista para mostrar los datos de la tabla
def display(request):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT episode_nb, title, director, producer, release_date FROM ex02_movies;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        if not rows:
            return HttpResponse("No data available")

        return render(request, 'ex02/display.html', {'movies': rows})

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
