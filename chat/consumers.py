import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user_name = text_data_json["username"]
        room_name = text_data_json["room"]

        await save_message(user_name, room_name, message)


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'username': user_name}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["username"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "username": user}))


@database_sync_to_async
def save_message(user_name, room_name, message):
    if message:
        room = Room.objects.get(slug=room_name)
        user = User.objects.get(username=user_name)
        Message.objects.create(room=room, user=user, content=message)
