from django.urls import path
from . import views

urlpatterns = [
    # Artículos
    path('', views.article_list, name='article_list'),  # Lista de artículos (raíz)
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),  # Detalle de un artículo
    path('articles/new/', views.publish, name='article_create'),  # Crear un artículo

    # Favoritos
    path('favourites/', views.favourites, name='favourite_list'),  # Lista de favoritos
    path('favourites/add/<int:pk>/', views.add_favourite, name='add_favourite'),  # Añadir a favoritos

    # Publicaciones y autenticación
    path('publications/', views.publications, name='publications'),  # Lista de publicaciones
    path('account/', views.account_view, name='account'),  # Vista del perfil de usuario
    path('register/', views.register, name='register'),  # Registro
    path('logout/', views.logout_view, name='logout'),  # Logout

    # AJAX
    path('ajax/login/', views.ajax_login, name='ajax_login'),  # Login vía AJAX
    path('ajax/logout/', views.ajax_logout, name='ajax_logout'),  # Logout vía AJAX
]