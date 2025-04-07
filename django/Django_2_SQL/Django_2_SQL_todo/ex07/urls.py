from django.urls import path
from . import views

urlpatterns = [
    path('load_opening_crawl/', views.load_opening_crawl, name='load_opening_crawl'),
    path('populate/', views.populate, name='populate'),
    path('display/', views.display, name='display'),
    path('update/', views.update, name='update'),
]
