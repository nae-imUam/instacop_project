# screensharing/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScreenSharingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'screen_sharing_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'screen_share_message',
                'message': message
            }
        )

    async def screen_share_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
