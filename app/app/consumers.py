import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .views import *

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):

        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            await self.send(text_data=json.dumps({
                'message': message
            }))
            
        except Exception as e:
            await self.send(text_data=json.dumps({
                'message': "Invalid request."
            }))