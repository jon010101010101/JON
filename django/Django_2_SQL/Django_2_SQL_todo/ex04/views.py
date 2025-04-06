from django.http import HttpResponse
from django.db import connection

def init(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex04_movies (
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

    results = []
    try:
        with connection.cursor() as cursor:
            for entry in data:
                try:
                    cursor.execute("""
                        INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                        VALUES (%s, %s, %s, %s, %s);
                    """, entry)
                    results.append(f"{entry[1]} inserted successfully.")
                except Exception as e:
                    results.append(f"Error inserting {entry[1]}: {str(e)}")
        return HttpResponse("<br>".join(results))
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

from django.http import HttpResponse
from django.db import connection

def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ex04_movies;")
            rows = cursor.fetchall()
            if not rows:
                return HttpResponse("No data available")

            # Aplica estilos CSS en línea directamente a la cadena HTML
            html = "<table style='width: 100%; border-collapse: collapse; margin: 20px 0; font-family: Arial, sans-serif;'>"  # General table styles
            html += "<thead style='background-color: #ADD8E6;'>"  # Light blue background for header
            html += "<tr>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Title</th>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Episode_Nb</th>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Opening_Crawl</th>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Director</th>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Producer</th>"
            html += "<th style='padding: 8px; text-align: left; text-transform: uppercase;'>Release_Date</th>"
            html += "</tr>"
            html += "</thead><tbody>"
            for row in rows:
                # Aplica el color azul muy clarito a las filas alternas
                if rows.index(row) % 2 == 0:
                    html += f"<tr style='background-color: #E0FFFF;'>"  # Azul muy clarito (Aqua)
                else:
                    html += "<tr>"
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[0]}</td>"  # Title
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[1]}</td>"  # Episode_Nb
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[2]}</td>"  # Opening_Crawl
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[3]}</td>"  # Director
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[4]}</td>"  # Producer
                html += f"<td style='padding: 8px; border-bottom: 1px solid #ddd;'>{row[5]}</td>"  # Release_Date
                html += "</tr>"
            html += "</tbody></table>"
            return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def remove(request):
    try:
        with connection.cursor() as cursor:
            if request.method == 'POST':
                title_to_remove = request.POST.get('title')
                cursor.execute("DELETE FROM ex04_movies WHERE title = %s;", [title_to_remove])
                message = f"{title_to_remove} removed successfully."

            cursor.execute("SELECT title FROM ex04_movies;")
            titles = cursor.fetchall()
            if not titles:
                return HttpResponse("No data available")

            html = f"<p>{message}</p>" if 'message' in locals() else ""
            html += "<form method='post'>"
            html += "<select name='title'>"
            for title in titles:
                html += f"<option value='{title[0]}'>{title[0]}</option>"
            html += "</select>"
            html += "<button type='submit'>Remove</button>"
            html += "</form>"
            return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
