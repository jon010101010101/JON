from django.shortcuts import render
from .models import People

def display(request):
    people = People.objects.filter(homeworld__climate__in=['windy', 'moder