from django import forms
from django.contrib.auth import get_user_model, authenticate
from .models import Tip

User = get_user_model()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        help_text="",
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username must be 150 characters or fewer.',
            'invalid': 'Username may contain only letters, numbers and @/./+/-/_ characters.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        error_messages={
            'required': 'Password is required.',
        }
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
        error_messages={
            'required': 'Please confirm your password.',
        }
    )

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

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(
        label="Username",
        error_messages={
            'required': 'Username is required.',
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        error_messages={
            'required': 'Password is required.',
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                self.add_error('username', "User not registered.")
                raise forms.ValidationError("User not registered.")
            user = authenticate(username=username, password=password)
            if user is None:
                self.add_error('password', "Incorrect password.")
                raise forms.ValidationError("Incorrect password.")
        return cleaned_data

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
