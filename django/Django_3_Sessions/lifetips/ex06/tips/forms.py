from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tip, CustomUser

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
        # Verifica si el email no está registrado
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("No user with this email was found.")
        return email
