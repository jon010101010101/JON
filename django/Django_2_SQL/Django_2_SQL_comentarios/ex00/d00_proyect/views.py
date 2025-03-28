from django.http import HttpResponse
from django.shortcuts import render
import psycopg2
from django.conf import settings

def init_view(request):
    try:
        # Database configuration from settings
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST']
        db_port = settings.DATABASES['default']['PORT']

        # Connect to PostgreSQL
        conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        cur = conn.cursor()

        # Query SQL para crear la tabla
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb INTEGER PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """

        # Ejecutar el query SQL
        cur.execute(create_table_sql)

        # Confirmar la transacción
        conn.commit()

        # Cerrar el cursor y la conexión
        cur.close()
        conn.close()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
