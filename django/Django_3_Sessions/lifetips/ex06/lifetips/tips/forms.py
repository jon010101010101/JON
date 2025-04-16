from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Tip, CustomUser  # Importa CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Incluye los campos que desees

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Share your tip...'
            }),
        }
        labels = {
            'content': 'Your tip',
        }
