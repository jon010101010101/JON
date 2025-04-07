from django.http import HttpResponse
from .models import Movies

# Vista para insertar datos en la tabla
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
        # Delete all existing movies
        Movies.objects.all().delete()

        # Insert the movies
        for entry in data:
            movie = Movies(**entry)
            movie.save()

        return HttpResponse("OK")  # Return "OK" if all insertions succeed

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")  # Return an error message if any insertion fails


# Vista para mostrar los datos de la tabla
def display(request):
    try:
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
            html += f"""
                <tr>
                    <td>{movie.episode_nb}</td>
                    <td>{movie.title}</td>
                    <td>{movie.director}</td>
                    <td>{movie.producer}</td>
                    <td>{movie.release_date}</td>
                </tr>
            """
        html += "</tbody></table>"
        return HttpResponse(html)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")