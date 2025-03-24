from django.shortcuts import render

def django_view(request):
    return render(request, 'django.html')

def display_view(request):
    return render(request, 'display.html')

def templates_view(request):
    return render(request, 'templates.html')

