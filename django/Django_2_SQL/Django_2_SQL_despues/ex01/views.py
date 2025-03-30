from django.http import HttpResponse
from django.db import connection
from ex01.models import Movies

def init(request):
    try:
        # Ejecutar las migraciones manualmente para crear la tabla
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex01_movies (
                    episode_nb SERIAL PRIMARY KEY,
                    title VARCHAR(64) UNIQUE NOT NULL,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                );
            """)
        return HttpResponse("OK: Tabla 'ex01_movies' creada correctamente.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
