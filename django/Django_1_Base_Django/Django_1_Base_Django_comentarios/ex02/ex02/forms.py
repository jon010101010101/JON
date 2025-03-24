# Importa el módulo forms de Django para crear formularios
from django import forms

# Define un formulario llamado LogForm
class LogForm(forms.Form):
    # Campo de texto llamado 'text'
    # Este campo permite ingresar una cadena de texto con una longitud máxima de 255 caracteres
    text = forms.CharField(max_length=255)
