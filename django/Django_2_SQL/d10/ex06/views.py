import os
import json
import psycopg2
from django.shortcuts import HttpResponse, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib import messages

DATABASE_NAME = "djangotraining"
DATABASE_USER = "djangouser"
DATABASE_PASSWORD = "secret"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def init(request):
    conn = get_db_connection()
    if not conn:
        return HttpResponse("Error: Could not connect to the database")

    try:
        cursor = conn.cursor()

        # SQL para crear la tabla
        create_table_query = """
            CREATE TABLE IF NOT EXISTS ex06_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(create_table_query)

        # Eliminar el trigger si ya existe
        cursor.execute("DROP TRIGGER IF EXISTS update_films_changetimestamp ON ex06_movies;")

        # Crear la función para actualizar el campo 'updated'
        create_function_query = """
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
        """
        cursor.execute(create_function_query)

        # Crear el trigger
        create_trigger_query = """
            CREATE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW EXECUTE PROCEDURE update_changetimestamp_column();
        """
        cursor.execute(create_trigger_query)

        conn.commit()
        return HttpResponse("OK")

    except psycopg2.Error as e:
        conn.rollback()
        return HttpResponse(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def populate(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur = conn.cursor()

        # Borrar todos los opening_crawl existentes
        cur.execute("UPDATE ex06_movies SET opening_crawl = NULL;")
        conn.commit()

        # Cargar los datos desde el archivo JSON
        json_file_path = os.path.join(settings.BASE_DIR, 'data', 'opening_crawl.json')

        with open(json_file_path, 'r') as f:
            movies_data = json.load(f)

        # Insertar datos desde el archivo JSON
        for title, opening_crawl in movies_data.items():
            if title == "The Phantom Menace":
                episode_nb = 1
                director = "George Lucas"
                producer = "Rick McCallum"
                release_date = "1999-05-19"
            elif title == "Attack of the Clones":
                episode_nb = 2
                director = "George Lucas"
                producer = "Rick McCallum"
                release_date = "2002-05-16"
            elif title == "Revenge of the Sith":
                episode_nb = 3
                director = "George Lucas"
                producer = "Rick McCallum"
                release_date = "2005-05-19"
            elif title == "A New Hope":
                episode_nb = 4
                director = "George Lucas"
                producer = "Gary Kurtz, Rick McCallum"
                release_date = "1977-05-25"
            elif title == "The Empire Strikes Back":
                episode_nb = 5
                director = "Irvin Kershner"
                producer = "Gary Kurtz, Rick McCallum"
                release_date = "1980-05-17"
            elif title == "Return of the Jedi":
                episode_nb = 6
                director = "Richard Marquand"
                producer = "Howard G. Kazanjian, George Lucas, Rick McCallum"
                release_date = "1983-05-25"
            elif title == "The Force Awakens":
                episode_nb = 7
                director = "J. J. Abrams"
                producer = "Kathleen Kennedy, J. J. Abrams, Bryan Burk"
                release_date = "2015-12-11"

            cur.execute("""
                INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date, opening_crawl)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (episode_nb) DO UPDATE
                SET title = %s, director = %s, producer = %s, release_date = %s, opening_crawl = %s;
            """, (episode_nb, title, director, producer, release_date, opening_crawl,
                  title, director, producer, release_date, opening_crawl))

        conn.commit()
        cur.close()
        conn.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {e}")

def display(request):
    conn = get_db_connection()
    if not conn:
        return HttpResponse("Error: Could not connect to the database")

    try:
        cursor = conn.cursor()
        # Modificar la consulta para ordenar por episode_nb
        cursor.execute("SELECT * FROM ex06_movies ORDER BY episode_nb;")
        movies = cursor.fetchall()

        # Imprimir para depuración
        print("Movies data:", movies)  # Verifica que se recuperen datos

        # Verifica la longitud de la lista de películas
        print("Number of movies:", len(movies))
        if movies:
            print("First movie:", movies[0])

        # Pasar los datos a la plantilla
        return render(request, 'ex06/display.html', {'movies': movies})

    except psycopg2.Error as e:
        return HttpResponse(f"Error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def update(request):
    conn = get_db_connection()
    if not conn:
        return render(request, 'ex06/update.html', {'message': "Error: No se pudo conectar a la base de datos"})

    if request.method == 'POST':
        selected_movie = request.POST.get('movie')
        new_opening_crawl = request.POST.get('opening_crawl')

        # Imprimir para depuración
        print("Selected movie:", selected_movie)
        print("New opening crawl:", new_opening_crawl)

        try:
            cursor = conn.cursor()
            update_query = """
                UPDATE ex06_movies
                SET opening_crawl = %s
                WHERE title = %s;
            """
            cursor.execute(update_query, (new_opening_crawl, selected_movie))
            conn.commit()

            # Comprobar cuántas filas se actualizaron
            if cursor.rowcount == 0:
                print("No rows were updated. Check if the title exists.")

            # Vuelve a obtener los títulos para actualizar la lista de películas en el formulario
            cursor.execute("SELECT title FROM ex06_movies;")
            movies = cursor.fetchall()
            movie_titles = [movie[0] for movie in movies]

            # Renderiza la plantilla con un mensaje de éxito y los datos actualizados
            return render(request, 'ex06/update.html', {
                'movies': movie_titles,
                'message': f"Opening crawl for '{selected_movie}' updated successfully!"
            })

        except psycopg2.Error as e:
            conn.rollback()
            # En caso de error, también recupera los títulos para no perder la lista en el formulario
            cursor.execute("SELECT title FROM ex06_movies;")
            movies = cursor.fetchall()
            movie_titles = [movie[0] for movie in movies]

            # Renderiza la plantilla con un mensaje de error
            return render(request, 'ex06/update.html', {
                'movies': movie_titles,
                'message': f"Error: {e}"
            })

        finally:
            if conn:
                cursor.close()
                conn.close()

    else:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT title, opening_crawl FROM ex06_movies;")
            movies = cursor.fetchall()

            if not movies:
                return render(request, 'ex06/update.html', {'message': "No data available."})

            # Pasa los títulos de las películas y el opening_crawl a la plantilla
            movie_titles = [movie[0] for movie in movies]
            opening_crawls = {movie[0]: movie[1] for movie in movies}  # Mapa de títulos a opening_crawl

            return render(request, 'ex06/update.html', {
                'movies': movie_titles,
                'opening_crawls': opening_crawls,
                'message': ''
            })

        except psycopg2.Error as e:
            return render(request, 'ex06/update.html', {'message': f"Error: {e}"})

        finally:
            if conn:
                cursor.close()
                conn.close()