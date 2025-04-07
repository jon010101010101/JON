from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render
import psycopg2
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

    try:
        with connection.cursor() as cursor:
            # Obtener los opening crawls existentes
            cursor.execute("SELECT title, opening_crawl FROM ex06_movies")
            existing_opening_crawls = dict(cursor.fetchall())

            # Borrar todos los datos existentes en la tabla
            cursor.execute("DELETE FROM ex06_movies;")

            # Insertar los datos con los opening crawls existentes
            for entry in data:
                title = entry["title"]
                opening_crawl = existing_opening_crawls.get(title, '')  # Usar el opening crawl existente si existe, sino, usar una cadena vacía
                cursor.execute(
                    "INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date, created, updated, opening_crawl) VALUES (%s, %s, %s, %s, %s, NOW(), NOW(), %s)",
                    (entry["episode_nb"], title, entry["director"], entry["producer"], entry["release_date"], opening_crawl),
                )
            connection.commit()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error inserting data: {str(e)}")

def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT episode_nb, title, director, producer, release_date, created, updated, opening_crawl FROM ex06_movies;")
            movies = cursor.fetchall()

            if not movies:
                return HttpResponse("No data available")

            return render(request, 'ex06/display.html', {'movies': movies})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def update(request):
    message = None
    if request.method == 'POST':
        title_to_update = request.POST.get('title')
        new_text = request.POST.get('opening_crawl')
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s", [new_text, title_to_update])
                connection.commit()
                message = f"The opening crawl for '{title_to_update}' has been updated successfully."
        except Exception as e:
            message = f"Error updating movie: {e}"

    try:
        with connection.cursor() as cursor:
             cursor.execute("SELECT title FROM ex06_movies;")
             movies = [row[0] for row in cursor.fetchall()]
    except:
        movies = None
   
    return render(request, 'ex06/update.html', {'movies': movies, 'message': message})

def load_opening_crawl(request):
    try:
        # Ruta al archivo JSON
        file_path = 'data/opening_crawl.json'

        # Abrir y cargar el contenido del archivo JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Conectar a la base de datos
        conn = psycopg2.connect(
            dbname='d42',
            user='djangouser',
            password='secret',
            host='localhost'  # Ajusta esto si tu base de datos está en otro host
        )
        cur = conn.cursor()

        # Actualizar la base de datos con los datos del JSON
        for title, opening_crawl in data.items():
            cur.execute("UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s", (opening_crawl, title))

        # Guardar los cambios
        conn.commit()

        # Cerrar la conexión
        cur.close()
        conn.close()

        return HttpResponse("Opening crawl data loaded successfully.")
    except FileNotFoundError:
        return HttpResponse("Error: File not found.")
    except json.JSONDecodeError:
        return HttpResponse("Error: Invalid JSON format.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
