from django.shortcuts import render
from .models import People
from .forms import SearchForm

def search_characters(request):
    results = []  # Lista para almacenar los resultados
    message = None  # Mensaje para mostrar en caso de error o sin resultados

    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Obtener los valores del formulario
            min_date = form.cleaned_data['min_release_date']
            max_date = form.cleaned_data['max_release_date']
            min_diameter = form.cleaned_data['min_planet_diameter']
            gender = form.cleaned_data['character_gender']

            # Filtrar personajes según los criterios
            characters = People.objects.filter(
                gender=gender,
                movies__release_date__range=(min_date, max_date),
                homeworld__diameter__gte=min_diameter
            ).select_related('homeworld').prefetch_related('movies').distinct()

            # Si hay personajes que cumplen los criterios, procesar los resultados
            if characters.exists():
                for character in characters:
                    for movie in character.movies.all():
                        results.append({
                            'character_name': character.name,
                            'gender': character.gender,
                            'movie_title': movie.title,
                            'homeworld_name': character.homeworld.name if character.homeworld else "No planet assigned",
                            'homeworld_diameter': character.homeworld.diameter if character.homeworld else "Unknown diameter",
                        })
            else:
                message = "Nothing corresponding to your research"

        else:
            message = "Please correct the errors below."

    return render(request, 'ex10/search.html', {
        'form': form,
        'results': results,
        'message': message,
    })
