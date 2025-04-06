from django.shortcuts import render
from .models import Planet, Person

def index(request):
    return render(request, 'ex09/index.html') 
