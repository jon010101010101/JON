from django.http import HttpResponse

def init_view(request):
    return HttpResponse("OK")
