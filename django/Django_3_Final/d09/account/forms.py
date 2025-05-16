from django import forms
from .models import Article

# Formulario para crear o editar artículos
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']