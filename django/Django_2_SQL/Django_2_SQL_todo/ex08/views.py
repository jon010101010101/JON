from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2
import os
import csv


class Init(View):
    def get(self, request):
        CREATE_TABLES = """
        CREATE TABLE IF NOT EXISTS ex08_planets(
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            climate VARCHAR,
            diameter INT,
            orbital_period INT,
            population BIGINT,
            rotation_period INT,
            surface_water REAL,
            terrain VARCHAR(128)
        );

        CREATE TABLE IF NOT EXISTS ex08_people(
            id SERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            birth_year VARCHAR(32),
            gender VARCHAR(32),
            eye_color VARCHAR(32),
            hair_color VARCHAR(32),
            height INT,
            mass REAL,
            homeworld VARCHAR(64) REFERENCES ex08_planets(name) ON DELETE CASCADE
        );
        """
        try:
            with psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            ) as conn:
                with conn.cursor() as curs:
                    curs.execute(CREATE_TABLES)
                conn.commit()
            return HttpResponse("OK: ex08_planets and ex08_people tables successfully created!")
        except Exception as e:
            return HttpResponse(f"Error: {e}")


class Populate(View):
    def get(self, request):
        try:
            with psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            ) as conn:
                with conn.cursor() as curs:
                    # Poblar ex08_planets
                    planet_path = os.path.join(settings.BASE_DIR, 'ex08', 'data', 'planets.csv')
                    with open(planet_path, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f, delimiter=',')
                        for row in reader:
                            try:
                                curs.execute(
                                    "INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population,"
                                    "rotation_period, surface_water, terrain) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                    (row[0], row[1], self.safe_int(row[2]), self.safe_int(row[3]),
                                     self.safe_int(row[4]), self.safe_int(row[5]),
                                     self.safe_float(row[6]), row[7])
                                )
                            except Exception as e:
                                print(f"Error inserting planet {row[0]}: {e}")

                    # Poblar ex08_people
                    people_path = os.path.join(settings.BASE_DIR, 'ex08', 'data', 'people.csv')
                    with open(people_path, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f, delimiter=',')
                        for row in reader:
                            try:
                                curs.execute(
                                    "INSERT INTO ex08_people (name, birth_year, gender, eye_color,"
                                    "hair_color, height, mass, homeworld) VALUES (%s, %s, %s, %s,"
                                    "%s, %s, %s, %s)",
                                    (row[0], row[1], row[2], row[3], row[4],
                                     self.safe_int(row[5]), self.safe_float(row[6]), row[7])
                                )
                            except Exception as e:
                                print(f"Error inserting person {row[0]}: {e}")

                conn.commit()
            return HttpResponse("OK: Data inserted into ex08_planets and ex08_people!")
        except Exception as e:
            return HttpResponse(f"Error populating data: {e}")

    def safe_int(self, value):
        """Convierte un valor a int o devuelve None si no es convertible."""
        if value in ['NULL', 'n/a', '']:
            return None
        try:
            return int(value)
        except ValueError:
            return None

    def safe_float(self, value):
        """Convierte un valor a float o devuelve None si no es convertible."""
        if value in ['NULL', 'n/a', '']:
            return None
        try:
            return float(value)
        except ValueError:
            return None


class Display(View):
    def get(self, request):
        try:
            with psycopg2.connect(
                dbname=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT'],
            ) as conn:
                with conn.cursor() as curs:
                    # Consulta para obtener personas de planetas con clima "windy"
                    SELECT_TABLE = """
                        SELECT
                            p.name AS person,
                            pl.name AS homeworld,
                            pl.climate AS climate
                        FROM
                            ex08_people p
                        LEFT JOIN ex08_planets pl ON p.homeworld = pl.name
                        WHERE pl.climate LIKE '%windy%'
                        ORDER BY p.name;
                    """
                    curs.execute(SELECT_TABLE)
                    datas = curs.fetchall()

            return render(request, 'ex08/display.html', {'datas': datas})
        except Exception as e:
            return HttpResponse(f"Error displaying data: {e}")
