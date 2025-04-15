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

    # Placeholder para géneros (se inicializa vacío)
    character_gender = forms.ChoiceField(
        label="Character gender",
        choices=[('', 'Select Gender')],  # Placeholder no seleccionable
        required=True,
        error_messages={'required': 'Please select a valid gender.'}
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener géneros únicos de la base de datos dinámicamente
        gender_choices = [('', 'Select Gender')]  # Placeholder no seleccionable
        gender_choices += [
            (gender, gender) for gender in People.objects.values_list('gender', flat=True).distinct() if gender
        ]
        
        # Actualizar las opciones del campo `character_gender`
        self.fields['character_gender'].choices = gender_choices

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
