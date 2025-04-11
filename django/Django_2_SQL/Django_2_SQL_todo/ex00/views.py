from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    """
    Esta vista inicializa la tabla ex00_movies en la base de datos PostgreSQL.
    """
    conn = None  # Inicializar la conexión
    cursor = None  # Inicializar el cursor
    try:
        # Conectar a la base de datos PostgreSQL utilizando la configuración de settings.py de Django
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        print("Connection to database successful")  # Verificar la conexión

        # Crear un objeto cursor para ejecutar consultas SQL
        cursor = conn.cursor()

        # Consulta SQL para crear la tabla ex00_movies si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            )
        """)

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Devolver una respuesta HTTP con "OK" si la creación de la tabla fue exitosa
        return HttpResponse("OK")

    except Exception as e:
        # Si ocurre una excepción, devolver una respuesta HTTP con un mensaje de error
        return HttpResponse(f"Error: {str(e)}")

    finally:
        # Asegurar que el cursor y la conexión se cierren en el bloque finally
        # Esto es importante para evitar fugas de recursos
        if cursor:
            cursor.close()  # Cerrar el cursor
        if conn:
            conn.close()  # Cerrar la conexión
