import psycopg2
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse  # Importa la función reverse

def init(request):
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"  # Ajusta esto si tu base de datos está en otro host
        )
        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        # Crear la tabla ex04_movies si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                episode_nb INTEGER PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        cur.close()
        conn.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def populate(request):
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"  # Ajusta esto si tu base de datos está en otro host
        )
        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        # Insertar los datos de las películas
        movies = [
            (1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"),
            (2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"),
            (3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"),
            (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
            (5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
            (6, "Return of the Jedi", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
            (7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
        ]

        for movie in movies:
            cur.execute("""
                INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (episode_nb) DO NOTHING
            """, movie)

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        cur.close()
        conn.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(str(e))


def display(request):
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"  # Ajusta esto si tu base de datos está en otro host
        )
        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        # Obtener todos los datos de la tabla ex04_movies
        cur.execute("SELECT episode_nb, title, director, producer, release_date FROM ex04_movies")
        movies = cur.fetchall()

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        cur.close()
        conn.close()

        # Crear la tabla HTML
        html = "<table>"
        html += "<tr><th>Episode</th><th>Title</th><th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        for movie in movies:
            html += f"<tr><td>{movie[0]}</td><td>{movie[1]}</td><td>{movie[2]}</td><td>{movie[3]}</td><td>{movie[4]}</td></tr>"
        html += "</table>"

        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(str(e))


def remove(request):
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname="djangotraining",
            user="djangouser",
            password="secret",
            host="localhost"  # Ajusta esto si tu base de datos está en otro host
        )
        # Crear un cursor para ejecutar consultas
        cur = conn.cursor()

        if request.method == 'POST':
            title_to_delete = request.POST.get('title')
            if title_to_delete:
                cur.execute("DELETE FROM ex04_movies WHERE title = %s", (title_to_delete,))
                conn.commit()

        # Obtener todos los títulos de películas para el formulario
        cur.execute("SELECT title FROM ex04_movies")
        movie_titles = [row[0] for row in cur.fetchall()]

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        cur.close()
        conn.close()

        # Crear el formulario HTML
        html = """
            <form method="post">
                <label for="title">Select a movie to delete:</label>
                <select name="title" id="title">
        """
        for title in movie_titles:
            html += f'<option value="{title}">{title}</option>'
        html += """
                </select>
                <button type="submit">Remove</button>
            </form>
        """

        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(str(e))
