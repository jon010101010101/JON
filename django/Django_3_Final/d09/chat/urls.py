from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),          # Lista de salas en /chat/rooms/
    path('<str:room_name>/', views.chat_room, name='chat_room'), # Sala de chat individual
]
