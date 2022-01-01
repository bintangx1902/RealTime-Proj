import json
from time import sleep
from random import randint
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(3_0):
            self.send(json.dumps({'messages': randint(1, 150)}))
            sleep(1)

        self.close()
