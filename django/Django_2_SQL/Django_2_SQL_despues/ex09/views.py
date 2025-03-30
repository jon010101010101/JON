from django.http import HttpResponse

def init(request):
    return HttpResponse(f"Vista 'init' de {__name__} funcionando correctamente.")
