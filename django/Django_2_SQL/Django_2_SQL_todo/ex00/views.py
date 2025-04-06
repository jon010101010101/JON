from django.conf import settings
from django.http import HttpResponse
import psycopg2

def init(request):
    try:
        # Conexión a la base de datos PostgreSQL
        conn = psycopg2.connect(
            dbname="d42",  # Nombre de la base de datos
            user="djangouser",  # Usuario configurado en docker-compose.yml
            password="secret",  # Contraseña configurada en docker-compose.yml
            host="localhost",  # Nombre del servicio definido en docker-compose.yml
            port="5432"
        )
        cursor = conn.cursor()

        # Crear una tabla si no existe
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            episode_nb SERIAL PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()
        return HttpResponse("OK")  # Respuesta exitosa si se crea la tabla

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")  # Mostrar el error si algo falla
