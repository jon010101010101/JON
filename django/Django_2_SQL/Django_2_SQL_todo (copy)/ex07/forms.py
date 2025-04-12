from django import forms
from .models import Movie

class UpdateForm(forms.Form):
    movie = forms.ModelChoiceField(queryset=Movie.objects.all(), label="Select a Movie")
    opening_crawl = forms.CharField(widget=forms.Textarea, label="New Opening Crawl")
