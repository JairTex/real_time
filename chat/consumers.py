from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala'] #Recuperando nome da sala
        self.room_group_name = f'chat_{self.room_name}' #retornando isso como nome da sala

        #Entrando na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        #Saindo da sala da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    #Recebendo mensagem do webSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']

        #Enviando mensagem para a sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'chat_message',
                'message' : mensagem
            }
        )

    #Recebendo mensagem da sala
    async def chat_message(self, event):
        mensagem = event['message']

        #Enviando a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'mensagem' : mensagem
        }))
