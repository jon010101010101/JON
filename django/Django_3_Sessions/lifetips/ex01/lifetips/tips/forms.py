from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if username and User.objects.filter(username=username).exists():
            self.add_error('username', "Username already taken.")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
