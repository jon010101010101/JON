from django.shortcuts import render
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
import datetime

def search_characters(request):
    """
    View for searching characters based on provided criteria.
    """
    results = []
    form = CharacterSearchForm()

    if request.method == 'POST':
        form = CharacterSearchForm(request.POST)
        if form.is_valid():
            min_release_date = form.cleaned_data.get('min_release_date')
            max_release_date = form.cleaned_data.get('max_release_date')
            min_planet_diameter = form.cleaned_data.get('min_planet_diameter')
            character_gender = form.cleaned_data.get('character_gender')

            # Example data - Replace with your actual data source
            all_results = [
                {'character_name': 'Leia Organa', 'gender': 'female', 'movie_title': 'Revenge of the Sith', 'homeworld_name': 'Alderaan', 'homeworld_diameter': 12500, 'release_date': date(2005, 5, 19)},
                {'character_name': 'Leia Organa', 'gender': 'female', 'movie_title': 'A New Hope', 'homeworld_name': 'Alderaan', 'homeworld_diameter': 12500, 'release_date': date(1977, 5, 25)},
                {'character_name': 'Luke Skywalker', 'gender': 'male', 'movie_title': 'A New Hope', 'homeworld_name': 'Tatooine', 'homeworld_diameter': 10465,  'release_date': date(1977, 5, 25)},
                {'character_name': 'Darth Vader', 'gender': 'male', 'movie_title': 'A New Hope', 'homeworld_name': 'Tatooine', 'homeworld_diameter': 10465, 'release_date': date(1977, 5, 25)},
                {'character_name': 'Beru Whitesun lars', 'gender': 'female', 'movie_title': 'Attack of the Clones', 'homeworld_name': 'Tatooine', 'homeworld_diameter': 10465, 'release_date': date(2002, 5, 16)},
                {'character_name': 'Obi-Wan Kenobi', 'gender': 'male', 'movie_title': 'Attack of the Clones', 'homeworld_name': 'Stewjon', 'homeworld_diameter': None, 'release_date': date(2002, 5, 16)},
            ]

            # Apply filters
            results = all_results
            if min_release_date:
                results = [r for r in results if r['release_date'] >= min_release_date]
            if max_release_date:
                results = [r for r in results if r['release_date'] <= max_release_date]
            if min_planet_diameter:
                results = [r for r in results if r['homeworld_diameter'] is not None and r['homeworld_diameter'] >= min_planet_diameter]
            if character_gender:
                results = [r for r in results if r['gender'] == character_gender]

    context = {'form': form, 'results': results}
    return render(request, 'ex10/search.html', context)


class CharacterSearchForm(forms.Form):
    """
    Form to search for characters with filtering options for release date,
    planet diameter and character gender.
    """
    min_release_date = forms.DateField(
        label="Min Release Date",
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'}),
    )
    max_release_date = forms.DateField(
        label="Max Release Date",
        required=False,
        widget=forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy', 'type': 'date'}),
    )
    min_planet_diameter = forms.IntegerField(
        label="Min Planet Diameter",
        required=False,
    )
    character_gender = forms.ChoiceField(
        label="Character Gender",
        choices=[('', 'Select Gender'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        required=False,
    )

    def clean_min_planet_diameter(self):
        """
        Validates that the minimum planet diameter is not negative.
        """
        min_planet_diameter = self.cleaned_data.get('min_planet_diameter')
        if min_planet_diameter is not None and min_planet_diameter < 0:
            raise ValidationError("Planet diameter cannot be negative.")
        return min_planet_diameter

    def clean(self):
        """
        Validates that the minimum date is not after the maximum date and that the years are within the allowed range.
        The maximum year must always be the current year.
        """
        cleaned_data = super().clean()
        min_release_date = cleaned_data.get('min_release_date')
        max_release_date = cleaned_data.get('max_release_date')

        # Get the current year
        current_year = datetime.date.today().year

        if min_release_date and max_release_date:
            # Validate year range: Min year is 2000, Max year is the current year
            min_year = 2000
            max_year = current_year

            if min_release_date.year < min_year:
                raise ValidationError(f"The Minimum Release Date year must be {min_year} or later.")
            if max_release_date.year > max_year:
                raise ValidationError(f"The Maximum Release Date year must be {max_year} or earlier.")

            if min_release_date > max_release_date:
                raise ValidationError(
                    "The minimum release date must be before the maximum release date."
                )

            # Validate date values
            try:
                date(min_release_date.year, min_release_date.month, min_release_date.day)
            except ValueError as e:
                raise ValidationError(f"Invalid Min Release Date: {e}")

            try:
                date(max_release_date.year, max_release_date.month, max_release_date.day)
            except ValueError as e:
                raise ValidationError(f"Invalid Max Release Date: {e}")

        return cleaned_data
