from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# This function returns a "Hello World!" text as an HTTP response.
def hello_world(request):
    return HttpResponse("Hello World!")
