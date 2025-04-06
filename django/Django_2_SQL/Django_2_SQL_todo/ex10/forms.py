from django import forms
from .models import People

class SearchForm(forms.Form):
    min_release_date = forms.DateField(
        label='Movies minimum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    max_release_date = forms.DateField(
        label='Movies maximum release date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    min_planet_diameter = forms.IntegerField(label='Planet diameter greater than')
    character_gender = forms.ChoiceField(label='Character gender', choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genders = People.objects.values_list('gender', flat=True).distinct()
        self.fields['character_gender'].choices = [('', '---------')] + [(g, g) for g in genders]
