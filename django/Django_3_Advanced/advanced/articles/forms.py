from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'synopsis', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 500px;',  # Más ancho visualmente
                'placeholder': 'Title'
            }),
            'synopsis': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,  # Más alto para textos largos
                'placeholder': 'Synopsis'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,  # Bastante alto para el contenido
                'placeholder': 'Content'
            }),
        }
