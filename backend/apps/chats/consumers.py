from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep 

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    

