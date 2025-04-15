from datetime import date
from django.shortcuts import render
from .models import Movies, People, Planets  # Importa el modelo Planets
from .forms import SearchForm

def search_view(request):
    results = []
    message = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            min_date = form.cleaned_data['min_release_date']
            max_date = form.cleaned_data['max_release_date']
            min_diameter = form.cleaned_data['planet_diameter_greater_than']
            gender = form.cleaned_data['character_gender']

            # Validar que la fecha máxima no sea menor que la mínima
            if max_date < min_date:
                form.add_error('max_release_date', "Maximum date cannot be earlier than minimum date.")
                return render(request, 'ex10/search.html', {'form': form, 'results': results, 'message': message})

            # Validar que las fechas no excedan el año actual
            current_year = date.today().year
            if max_date.year > current_year or min_date.year > current_year:
                form.add_error('max_release_date', f"Dates must not exceed the current year ({current_year}).")
                return render(request, 'ex10/search.html', {'form': form, 'results': results, 'message': message})

            # Filtrar películas y personajes según los criterios
            movies = Movies.objects.filter(release_date__range=(min_date, max_date))
            
            # Filtrar a las personas por género Y diámetro del planeta
            people = People.objects.filter(
                gender=gender,
                homeworld__diameter__gte=min_diameter  # Accede al diámetro a través de homeworld
            )

            # Generar combinaciones únicas de resultados
            for movie in movies:
                for person in movie.characters.filter(gender=gender, homeworld__diameter__gte=min_diameter):
                    results.append({
                        'movie_title': movie.title,
                        'character_name': person.name,
                        'character_gender': person.gender,
                        'homeworld_name': person.homeworld.name if person.homeworld else 'N/A',
                        'homeworld_diameter': person.homeworld.diameter if person.homeworld else 'N/A',
                    })

            # Ordenar los resultados por los campos especificados
            results.sort(key=lambda x: (
                x['movie_title'],          # Ordenar por título de película
                x['character_name'],       # Ordenar por nombre del personaje
                x['character_gender'],     # Ordenar por género
                x['homeworld_name'],       # Ordenar por nombre del planeta
                x['homeworld_diameter']    # Ordenar por diámetro del planeta
            ))

            if not results:
                message = "No results found."
        else:
            # Si el formulario no es válido, se pasan los errores automáticamente
            message = "Please correct the errors below."
    else:
        form = SearchForm()

    return render(request, 'ex10/search.html', {
        'form': form,
        'results': results,
        'message': message,
        'errors': form.errors if not form.is_valid() else None  # Pasar errores si el formulario no es válido
    })
