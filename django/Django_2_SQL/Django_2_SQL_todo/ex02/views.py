from django.http import HttpResponse
from django.db import connection

# Vista para crear la tabla
def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex02_movies (
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vista para insertar datos en la tabla
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
            # Borrar todos los datos existentes en la tabla
            cursor.execute("DELETE FROM ex02_movies;")

            for episode_nb, title, director, producer, release_date in data:
                try:
                    cursor.execute("""
                        INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s);
                    """, (episode_nb, title, director, producer, release_date))
                except Exception as e:
                    return HttpResponse(f"Error: {str(e)}") # Returns error if any insertion fails

            return HttpResponse("OK") # If all insertions succeed, return OK
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

# Vista para mostrar los datos de la tabla
def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ex02_movies;")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")

            # Se añade un estilo CSS básico al HTML
            html = """
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                    font-family: Arial, sans-serif;
                    border: 1px solid black; /* Borde negro para la tabla */
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                    border: 1px solid black; /* Borde negro para las celdas */
                }
                th {
                    background-color: #007BFF; /* Azul */
                    color: white;
                }
                tr:nth-child(even) {
                    background-color: #e0f2f7; /* Azul claro */
                }
                tr:nth-child(odd) {
                    background-color: white; /* Blanco */
                }
            </style>
            <table>
                <tr>
                    <th>Episode</th>
                    <th>Title</th>
                    <th>Director</th>
                    <th>Producer</th>
                    <th>Release Date</th>
                </tr>
            """
            for row in rows:
                html += f"""
                <tr>
                    <td>{row[1]}</td>
                    <td>{row[0]}</td>
                    <td>{row[3]}</td>
                    <td>{row[4]}</td>
                    <td>{row[5]}</td>
                </tr>
                """
            html += "</table>"
            return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")