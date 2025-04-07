# ex05/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movies
from django.db import IntegrityError
from datetime import date
from django.views.decorators.csrf import csrf_exempt

def populate(request):
    data = [
        {"episode_nb": 1, "title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(1999, 5, 19)},
        {"episode_nb": 2, "title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2002, 5, 16)},
        {"episode_nb": 3, "title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2005, 5, 19)},
        {"episode_nb": 4, "title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1977, 5, 25)},
        {"episode_nb": 5, "title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1980, 5, 17)},
        {"episode_nb": 6, "title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": date(1983, 5, 25)},
        {"episode_nb": 7, "title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": date(2015, 12, 11)},
    ]

    for entry in data:
        try:
            movie, created = Movies.objects.update_or_create(
                episode_nb=entry["episode_nb"],
                defaults={
                    'title': entry["title"],
                    'director': entry["director"],
                    'producer': entry["producer"],
                    'release_date': entry["release_date"]
                }
            )
            if created:
                print(f"{entry['title']} inserted successfully.")
            else:
                print(f"{entry['title']} updated successfully.")
        except IntegrityError as e:
            print(f"Error inserting {entry['title']}: {e}")
    return HttpResponse("OK")

def display(request):
    movies = Movies.objects.all()

    if not movies:
        return HttpResponse("No data available")

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
            width: 100%; /* Ancho al 100% */
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
            background-color: #007bff; /* Azul */
            color: white;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #e0f2f7; /* Azul claro para filas pares */
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
        html += f"""
            <tr>
                <td>{movie.episode_nb}</td>
                <td>{movie.title}</td>
                <td>{movie.director}</td>
                <td>{movie.producer}</td>
                <td>{movie.release_date}</td>
            </tr>
        """

    html += """
        </tbody>
    </table>
    """

    return HttpResponse(html)

@csrf_exempt
def remove(request):
    if request.method == 'POST':
        title_to_remove = request.POST.get('title')
        try:
            movie = Movies.objects.get(title=title_to_remove)
            movie.delete()
        except Movies.DoesNotExist:
            pass  # Movie already deleted or does not exist
        # Redirect to the same remove page after deletion
        return redirect(request.path_info)

    movies = Movies.objects.all()

    if not movies:
        return HttpResponse("No data available")

    html = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        form {
            width: 100%;
            max-width: 400px;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            display: flex;
            flex-direction: column;
        }
        select {
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ced4da;
            border-radius: 6px;
            box-sizing: border-box;
            font-size: 16px;
            color: #495057;
            background-color: #fff;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 14px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        h1 {
            color: #007bff;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    <h1>Remove a Movie</h1>
    <form method="post">
        <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
        <label for="title">Select a Movie:</label>
        <select name="title" id="title">
    """

    for movie in movies:
        html += f"""
            <option value="{movie.title}">{movie.title}</option>
        """

    html += """
        </select>
        <button type="submit">Remove</button>
    </form>
    """

    return HttpResponse(html)
