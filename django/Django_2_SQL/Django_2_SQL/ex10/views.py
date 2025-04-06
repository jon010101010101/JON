from django.shortcuts import render
from .models import Planet, Person

def index(request):
    return render(request, 'ex10/index.html')  
