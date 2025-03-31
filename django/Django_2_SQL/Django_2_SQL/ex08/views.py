import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Planet, Person
from django.db import transaction
from django.db.utils import IntegrityError

def init(request):
    # Crear las tablas (ya se hace con las migraciones)
    return HttpResponse("Tables created.")

def populate(request):
    try:
        with transaction.atomic():
            # Cargar Planets
            with open('path/to/planets.csv', 'r') as planets_file:
                reader = csv.DictReader(planets_file)
                for row in reader:
                    planet = Planet(
                        name=row['name'],
                        climate=row['climate'],
                        diameter=row['diameter'],
                        orbital_period=row['orbital_period'],
                        population=row['population'],
                        rotation_period=row['rotation_period'],
                        surface_water=row['surface_water'],
                        terrain=row['terrain']
                    )
                    planet.save()

            # Cargar People
            with open('path/to/people.csv', 'r') as people_file:
                reader = csv.DictReader(people_file)
                for row in reader:
                    person = Person(
                        name=row['name'],
                        birth_year=row['birth_year'],
                        gender=row['gender'],
                        eye_color=row['eye_color'],
                        hair_color=row['hair_color'],
                        height=row['height'],
                        mass=row['mass'],
                        homeworld=row['homeworld']
                    )
                    person.save()

        return HttpResponse("OK")
    except IntegrityError as e:
        return HttpResponse(f"Error: {str(e)}")

def display(request):
    try:
        people = Person.objects.filter(homeworld__climate__in=['windy', 'moderately windy']).order_by('name')
        if not people.exists():
            return HttpResponse("No data available")

        result = "<br>".join([f"{person.name} - {person.homeworld} - {person.homeworld.climate}" for person in people])
        return HttpResponse(result)
    except Exception as e:
        return HttpResponse("No data available")