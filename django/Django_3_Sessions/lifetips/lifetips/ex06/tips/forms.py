from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Tip, CustomUser

# SOLO CON INSTALACION django-simple-captcha
try:
    from captcha.fields import CaptchaField
    CAPTCHA_INSTALLED = True
except ImportError:
    CAPTCHA_INSTALLED = False

class TipForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or len(content.strip()) < 5:
            raise forms.ValidationError("The tip content must be at least 5 characters long.")
        return content

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different one.")
        return email

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("The email field is required.")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("No user with this email was found.")
        return email

class CustomAuthenticationForm(AuthenticationForm): 
    if CAPTCHA_INSTALLED:
        captcha = CaptchaField(required=False, label="Please solve the captcha")

    def __init__(self, *args, **kwargs):
        show_captcha = kwargs.pop('show_captcha', False)
        super().__init__(*args, **kwargs)
        if CAPTCHA_INSTALLED and not show_captcha:
            self.fields.pop('captcha')

# --- REGISTRO PERSONALIZADO PARA EVITAR EL ERROR DE IMPORT ---
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
