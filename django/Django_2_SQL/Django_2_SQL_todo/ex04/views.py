import psycopg2
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

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
                html = """
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        padding: 20px;
                    }
                    table {
                        border-collapse: collapse;
                        width: 100%;
                        margin: 20px auto;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        background-color: white;
                    }
                    th, td {
                        padding: 12px 15px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }
                    th {
                        background-color: #007bff;
                        color: white;
                        font-weight: bold;
                    }
                    tr:nth-child(even) {
                        background-color: #e0f2f7;
                    }
                    tr:hover {
                        background-color: #f5f5f5;
                    }
                </style>
                <h1>Movies</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Episode</th>
                            <th>Title</th>
                            <th>Director</th>
                            <th>Producer</th>
                            <th>Release Date</th>
                        </tr>
                    </thead>
                    <tbody>
                """

                for movie in movies:
                    episode_nb, title, director, producer, release_date = movie
                    html += f"""
                        <tr>
                            <td>{episode_nb}</td>
                            <td>{title}</td>
                            <td>{director}</td>
                            <td>{producer}</td>
                            <td>{release_date}</td>
                        </tr>
                    """

                html += """
                    </tbody>
                </table>
                """
                return HttpResponse(html)
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

            html = f"""
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    padding: 20px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }}
                .message {{
                    background-color: #dff0d8;
                    color: #3c763d;
                    padding: 10px;
                    margin-bottom: 20px;
                    border: 1px solid #d6e9c6;
                    border-radius: 4px;
                }}
                form {{
                    width: 50%;
                    margin: 20px auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    border-radius: 4px;
                }}
                select {{
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 15px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    box-sizing: border-box;
                }}
                button {{
                    background-color: #007bff;
                    color: white;
                    padding: 10px 15px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    width: 100%; /* Make the button wider */
                }}
                button:hover {{
                    background-color: #0056b3;
                }}
                h1 {{
                    color: #007bff;
                    text-align: center;
                    margin-bottom: 20px;
                }}
            </style>
            <h1>Remove a Movie</h1>
            """
            if message:
                html += f'<div class="message">{message}</div>'
            html += """
            <form method='post'>
                <select name='title'>
            """
            for title in titles:
                html += f"<option value='{title}'>{title}</option>"
            html += """
                </select>
                <button type='submit'>Remove</button>
            </form>
            """
            return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
