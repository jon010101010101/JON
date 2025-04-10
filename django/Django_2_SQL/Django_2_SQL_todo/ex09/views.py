from django.shortcuts import render
from .models import People
from django.db.models import Q

def display(request):
    people = People.objects.filter(
        Q(homeworld__climate__icontains='windy') | Q(homeworld__climate__icontains='moderately windy')
    ).select_related('homeworld').order_by('name')

    if people.exists():
        return render(request, 'ex09/display.html', {'people': people})
    else:
        message = "No data available, please use the following command line before use: python manage.py loaddata ex09/fixtures/ex09_initial_data.json"
        return render(request, 'ex09/display.html', {'message': message})
