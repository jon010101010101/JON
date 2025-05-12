import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    users_in_room = {}

    async def connect(self):
        from .models import ChatRoom 
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.username = self.scope["user"].username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        ChatConsumer.users_in_room.setdefault(self.room_name, set()).add(self.username)
        await self.send_user_list()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.username} has joined the chat',
                'username': 'System'
            }
        )

    async def disconnect(self, close_code):
        users = ChatConsumer.users_in_room.get(self.room_name, set())
        users.discard(self.username)
        await self.send_user_list()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.username} has left the chat',
                'username': 'System'
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await sync_to_async(self.save_message)(self.room_name, username, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))

    async def send_user_list(self):
        user_list = list(ChatConsumer.users_in_room.get(self.room_name, []))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list',
                'user_list': user_list
            }
        )

    async def user_list(self, event):
        await self.send(text_data=json.dumps({
            'user_list': event['user_list']
        }))

    def save_message(self, room_name, username, message):
        from .models import ChatRoom, Message
        from django.contrib.auth.models import User
        room = ChatRoom.objects.get(name=room_name)
        user = User.objects.get(username=username)
        Message.objects.create(room=room, user=user, content=message)
