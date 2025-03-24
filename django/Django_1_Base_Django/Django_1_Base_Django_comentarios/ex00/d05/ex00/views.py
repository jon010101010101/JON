from django.shortcuts import render  # Importa la función 'render' de Django para renderizar plantillas HTML

# Define la vista 'markdown_cheatsheet'
def markdown_cheatsheet(request):
    # Renderiza la plantilla 'index.html' ubicada en la carpeta 'ex00'
    # El objeto 'request' representa la solicitud HTTP realizada por el usuario
    return render(request, 'ex00/index.html')
