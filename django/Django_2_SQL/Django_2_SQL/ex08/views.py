from django.shortcuts import render
from .models import Planet, Person

def index(request):
    return render(request, 'ex08/index.html')  # Asegúrate de que este template exista
