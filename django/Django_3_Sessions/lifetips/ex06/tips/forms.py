from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tip, CustomUser

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')
