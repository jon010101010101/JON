from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='articles'),  # La raíz muestra la lista de artículos
    path('articles/', views.article_list, name='articles'),  # También accesible desde /articles/
    path('publications/', views.publications, name='publications'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('publish/', views.publish, name='publish'),
    path('favourites/', views.favourites, name='favourites'),
    path('add-favourite/<int:pk>/', views.add_favourite, name='add-favourite'),
    path('favourite-added/', views.favourite_added, name='favourite-added'),
    path('already-favourite/', views.already_favourite, name='already-favourite'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
    path('test-template/', views.test_template),
    path('account/', views.account_view, name='account'),  # Login en /account/
    path('ajax_login/', views.ajax_login, name='ajax_login'),
    path('ajax_logout/', views.ajax_logout, name='ajax_logout'),
]
