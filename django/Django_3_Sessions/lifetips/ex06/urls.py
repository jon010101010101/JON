from django.urls import path
from tips import views

urlpatterns = [
    # Página principal de tips
    path('', views.home, name='home'),  # Página de inicio de la app "tips"

    # Funciones relacionadas con los tips
    path('create/', views.create_tip, name='create_tip'),  # Crear un nuevo tip
    path('<int:tip_id>/vote/<str:vote_type>/', views.vote_tip, name='vote_tip'),  # Votar (upvote/downvote)
    path('<int:tip_id>/delete/', views.delete_tip, name='delete_tip'),  # Eliminar un tip
    path('list/', views.tips_list, name='tips_list'),  # Listar todos los tips
]