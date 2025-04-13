import psycopg2
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db import IntegrityError

def init(request):
    """
    Crea la tabla ex04_movies si no existe.
    Creates the ex04_movies table if it doesn't exist.
    """
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
    """
    Elimina los datos existentes e inserta datos de películas.
    Deletes existing data and inserts movie data.
    """
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
                try:
                    cursor.execute(
                        "INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date) VALUES (%s, %s, %s, %s, %s)",
                        (episode_nb, title, director, producer, release_date),
                    )
                except IntegrityError as e:
                    # Manejo de errores de integridad (ej., clave primaria duplicada)
                    # Handling integrity errors (e.g., duplicate primary key)
                    return HttpResponse(f"Error inserting {title}: {str(e)}")
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    """
    Recupera y muestra los datos de la tabla ex04_movies.
    Retrieves and displays data from the ex04_movies table.
    """
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

# @csrf_exempt   porque deshabilita la protección CSRF
def remove(request):
    """
    Muestra un formulario para eliminar películas y maneja la eliminación.
    Displays a form to remove movies and handles the deletion.
    """
    message = ""
    try:
        with connection.cursor() as cursor:
            if request.method == 'POST':
                title_to_remove = request.POST.get('title')
                # Usar parámetros para evitar la inyección SQL
                # Use parameters to prevent SQL injection
                cursor.execute("DELETE FROM ex04_movies WHERE title = %s", [title_to_remove])
                connection.commit()
                message = f"{title_to_remove} removed successfully."

            cursor.execute("SELECT title FROM ex04_movies;")
            titles = [row[0] for row in cursor.fetchall()]

            if not titles:
                return HttpResponse("No data available")

            return render(request, 'ex04/remove.html', {'titles': titles, 'message': message})
    except Exception as e:
        message = f"Error removing movie: {str(e)}"
        cursor.execute("SELECT title FROM ex04_movies;")
        titles = [row[0] for row in cursor.fetchall()]
        return render(request, 'ex04/remove.html', {'titles': titles, 'message': message})
