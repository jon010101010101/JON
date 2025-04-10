from django.shortcuts import render, HttpResponse
from django.db import connection 
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # Importar settings
from datetime import date
import os
import csv
import psycopg2


@csrf_exempt
def init(request):
    try:
        with connection.cursor() as cursor:
            # Eliminar las tablas si existen
            cursor.execute("DROP TABLE IF EXISTS ex08_people CASCADE;")
            cursor.execute("DROP TABLE IF EXISTS ex08_planets CASCADE;")

            # Crear la tabla ex08_planets
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_planets (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    climate VARCHAR(128) NULL,
                    diameter INT NULL,
                    orbital_period INT NULL,
                    population BIGINT NULL,
                    rotation_period INT NULL,
                    surface_water REAL NULL,
                    terrain VARCHAR(128) NULL
                );
            """)

            # Crear la tabla ex08_people con clave foránea
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    birth_year VARCHAR(32) NULL,
                    gender VARCHAR(32) NULL,
                    eye_color VARCHAR(32) NULL,
                    hair_color VARCHAR(32) NULL,
                    height INT NULL,
                    mass REAL NULL,
                    homeworld_id INT REFERENCES ex08_planets(id) ON DELETE CASCADE
                );
            """)

        return render(request, 'ex08/init.html', {'message': "Tablas creadas exitosamente."})
    except Exception as e:
        return render(request, 'ex08/init.html', {'message': f"Error: {e}"})

@csrf_exempt
def populate(request):
    try:
        # Definir las rutas de los archivos CSV
        planets_file_path = os.path.join(os.path.dirname(__file__), 'data', 'planets.csv')
        people_file_path = os.path.join(os.path.dirname(__file__), 'data', 'people.csv')

        # Función para convertir "NULL" en valores nulos (None)
        def convert_null(value):
            return None if value == "NULL" or value == "" else value

        # Poblar la tabla ex08_planets
        with open(planets_file_path, newline='') as planets_file:
            planets_reader = csv.reader(planets_file, delimiter='\t')  # Usar tabulación como delimitador
            with connection.cursor() as cursor:
                for row in planets_reader:
                    try:
                        # Convertir "NULL" a None
                        row = [convert_null(value) for value in row]
                        cursor.execute("""
                            INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT (name) DO NOTHING;
                        """, row)
                    except Exception as e:
                        return HttpResponse(f"Error insertando datos en ex08_planets: {e}")

        # Poblar la tabla ex08_people
        with open(people_file_path, newline='') as people_file:
            people_reader = csv.reader(people_file, delimiter='\t')  # Usar tabulación como delimitador
            with connection.cursor() as cursor:
                for row in people_reader:
                    try:
                        # Convertir "NULL" a None
                        row = [convert_null(value) for value in row]
                        
                        # Obtener el id del planeta correspondiente al homeworld
                        cursor.execute("SELECT id FROM ex08_planets WHERE name = %s;", [row[7]])
                        planet_id = cursor.fetchone()
                        
                        if planet_id is not None:
                            planet_id = planet_id[0]  # Extraer el id del resultado

                            # Insertar los datos en ex08_people
                            cursor.execute("""
                                INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld_id)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                ON CONFLICT (name) DO NOTHING;
                            """, [row[0], row[1], row[2], row[3], row[4], row[5], row[6], planet_id])
                    except Exception as e:
                        return HttpResponse(f"Error insertando datos en ex08_people: {e}")

        return HttpResponse("OK")
    except FileNotFoundError as e:
        return HttpResponse(f"Archivo no encontrado: {e}")
    except Exception as e:
        return HttpResponse(f"Ocurrió un error: {e}")


def display(request):
    try:
        with connection.cursor() as cursor:
            # Consulta SQL para obtener los personajes, sus planetas natales y el clima
            cursor.execute("""
                SELECT p.name AS person_name, pl.name AS planet_name, pl.climate AS planet_climate
                FROM ex08_people p
                JOIN ex08_planets pl ON p.homeworld_id = pl.id
                WHERE pl.climate LIKE '%windy%' OR pl.climate LIKE '%moderately windy%'
                ORDER BY p.name ASC;
            """)
            rows = cursor.fetchall()

        # Verificar si hay datos disponibles y pasarlos a la plantilla
        return render(request, 'ex08/display.html', {'data': rows})
    except Exception as e:
        return render(request, 'ex08/display.html', {'error': str(e)})
