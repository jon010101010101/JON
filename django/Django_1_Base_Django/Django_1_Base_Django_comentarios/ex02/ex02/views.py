# Importa las funciones render y redirect para manejar solicitudes y redirecciones
from django.shortcuts import render, redirect

# Importa la configuración del proyecto desde settings.py
from django.conf import settings

# Importa el formulario LogForm desde forms.py
from .forms import LogForm

# Importa el modelo LogEntry desde models.py
from .models import LogEntry

# Importa el módulo datetime para trabajar con fechas y horas
from datetime import datetime

# Define la vista principal para la funcionalidad ex02
def ex02_view(request):
    # Si la solicitud es de tipo POST (envío de formulario)
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados
        form = LogForm(request.POST)
        # Verifica si los datos del formulario son válidos
        if form.is_valid():
            # Obtiene el texto ingresado en el formulario
            text = form.cleaned_data['text']
            # Crea un nuevo registro en la base de datos con el texto ingresado
            LogEntry.objects.create(text=text)
            
            # Obtiene la marca de tiempo actual en formato 'YYYY-MM-DD HH:MM:SS'
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Crea una entrada de log con la marca de tiempo y el texto
            log_entry = f"{timestamp}: {text}\n"
            
            # Abre el archivo de log en modo 'append' (agregar) y escribe la entrada
            with open(settings.LOG_FILE_PATH, 'a') as log_file:
                log_file.write(log_entry)
            
            # Redirige al usuario a la misma página después de procesar el formulario
            return redirect('ex02')
    else:
        # Si la solicitud no es POST, crea un formulario vacío
        form = LogForm()
    
    # Recupera todos los registros de log ordenados por marca de tiempo descendente
    logs = LogEntry.objects.all().order_by('-timestamp')
    
    # Renderiza la plantilla 'ex02/index.html' con el formulario y los registros de log
    return render(request, 'ex02/index.html', {'form': form, 'logs': logs})
