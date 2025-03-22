from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Esta función devuelve un texto "Hello World!" como respuesta HTTP.
def hello_world(request):
    return HttpResponse("Hello World!")
