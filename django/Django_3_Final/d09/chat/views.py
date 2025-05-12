from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, Message

@login_required
def room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    last_messages = Message.objects.filter(room=room).order_by('-timestamp')[:3][::-1]
    return render(request, 'chat/chat_room.html', {'room': room, 'last_messages': last_messages})

@login_required
def favourites(request):
    favs = UserFavouriteArticle.objects.filter(user=request.user)
    return render(request, 'account/favourites.html', {'favs': favs})
