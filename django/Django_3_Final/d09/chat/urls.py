from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),  # Esto será para el chat en tiempo real
]
