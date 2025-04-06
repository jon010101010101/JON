from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.init),
    path('populate/', views.populate),
    path('display/', views.display),
    path('update/', views.update),
    path('load_opening_crawl/', views.load_opening_crawl), ]
