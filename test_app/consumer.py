import json
from time import sleep
from random import randint
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    async def connect(self):
        self.accept()
        for i in range(1_000):
            await self.send(json.dumps({"messages": randint(1, 100)}))
            sleep(1)
