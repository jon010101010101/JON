# Importa la función render del módulo django.shortcuts
# render se usa para renderizar plantillas HTML y devolverlas como respuesta
from django.shortcuts import render

# Vista para la página 'django'
def django_view(request):
    # Renderiza la plantilla 'django.html' y la devuelve como respuesta
    return render(request, 'django.html')

# Vista para la página 'display'
def display_view(request):
    # Renderiza la plantilla 'display.html' y la devuelve como respuesta
    return render(request, 'display.html')

# Vista para la página 'templates'
def templates_view(request):
    # Renderiza la plantilla 'templates.html' y la devuelve como respuesta
    return render(request, 'templates.html')
