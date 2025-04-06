from django.shortcuts import render
from .models import People
from .forms import SearchForm

def search_characters(request):
    results = []
    message = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            min_date = form.cleaned_data['min_release_date']
            max_date = form.cleaned_data['max_release_date']
            min_diameter = form.cleaned_data['min_planet_diameter']
            gender = form.cleaned_data['character_gender']

            # Filter characters directly using all criteria in the ORM
            characters = People.objects.filter(
                gender=gender,
                movies__release_date__range=(min_date, max_date),
                homeworld__diameter__gte=min_diameter
            ).select_related('homeworld').prefetch_related('movies').distinct()

            # Build results if characters match the criteria
            if characters.exists():
                for character in characters:
                    for movie in character.movies.filter(release_date__range=(min_date, max_date)):
                        results.append({
                            'character_name': character.name,
                            'gender': character.gender,
                            'movie_title': movie.title,
                            'homeworld_name': character.homeworld.name if character.homeworld else "No planet assigned",
                            'homeworld_diameter': character.homeworld.diameter if character.homeworld else "Unknown diameter",
                        })
            else:
                # Custom message based on missing or invalid filters
                if not min_date or not max_date:
                    message = "No characters found because no valid date range was provided."
                elif not gender:
                    message = "No characters found because no valid gender was provided."
                elif not min_diameter:
                    message = "No characters found because no valid minimum planet diameter was provided."
                else:
                    message = "No characters match the specified criteria."
        else:
            message = "Please check the entered data and try again."
    else:
        form = SearchForm()

    return render(request, 'ex10/search.html', {
        'form': form,
        'results': results,
        'message': message,
    })
