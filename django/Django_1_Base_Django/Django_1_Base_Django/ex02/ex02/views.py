from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LogForm
from .models import LogEntry
from datetime import datetime

def ex02_view(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            LogEntry.objects.create(text=text)
            
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp}: {text}\n"
            
            with open(settings.LOG_FILE_PATH, 'a') as log_file:
                log_file.write(log_entry)
            
            return redirect('ex02')
    else:
        form = LogForm()
    
    logs = LogEntry.objects.all().order_by('-timestamp')
    return render(request, 'ex02/index.html', {'form': form, 'logs': logs})
