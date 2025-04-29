import random
import time
from django.conf import settings
from django.shortcuts import render

def home(request):
    now = time.time()
    anonymous_name = request.session.get('anonymous_name')
    timestamp = request.session.get('anonymous_name_timestamp', 0)

    # Si no hay nombre o han pasado más de 42 segundos, asigna uno nuevo
    if not anonymous_name or now - timestamp > 42:
        anonymous_name = random.choice(settings.USERNAME_LIST)
        request.session['anonymous_name'] = anonymous_name
        request.session['anonymous_name_timestamp'] = now

    return render(request, 'home.html', {'anonymous_name': anonymous_name})
