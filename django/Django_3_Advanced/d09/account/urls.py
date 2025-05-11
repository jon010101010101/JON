from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
    path('favourites/', views.favourites, name='favourites'),
    path('add-favourite/<int:pk>/', views.add_favourite, name='add-favourite'),
    path('favourite-added/', views.favourite_added, name='favourite-added'),
    path('already-favourite/', views.already_favourite, name='already-favourite'),
    path('publications/', views.publications, name='publications'),
    path('publish/', views.publish, name='publish'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
