import datetime
from django import forms
from .models import People

class SearchForm(forms.Form):
    min_release_date = forms.DateField(
        label="Movies minimum release date",
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    max_release_date = forms.DateField(
        label="Movies maximum release date",
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    planet_diameter_greater_than = forms.IntegerField(
        label="Planet diameter greater than",
        min_value=0,
        error_messages={'min_value': 'Diameter cannot be negative.'}
    )

    # Obtener géneros únicos de la base de datos y agregar placeholder
    gender_choices = [('', 'Gender')]  # Placeholder no seleccionable
    gender_choices += [(gender, gender) for gender in People.objects.values_list('gender', flat=True).distinct() if gender]

    character_gender = forms.ChoiceField(
        label="Character gender",
        choices=gender_choices,
        required=True,
        error_messages={'required': 'Please select a valid gender.'}
    )

    # Validación de fechas
    def clean(self):
        cleaned_data = super().clean()
        min_date = cleaned_data.get('min_release_date')
        max_date = cleaned_data.get('max_release_date')

        if min_date and max_date:
            if max_date < min_date:
                self.add_error('max_release_date', "Maximum date cannot be earlier than minimum date.")
            
            current_year = datetime.date.today().year
            if max_date.year > current_year:
                self.add_error('max_release_date', f"Date cannot exceed current year ({current_year}).")

        return cleaned_data

