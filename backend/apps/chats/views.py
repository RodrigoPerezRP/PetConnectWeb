from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 

class GetMessagesOfChat(APIView):
    def get(self,request,*args,**kwargs):
        idChat = kwargs.get('id')
        chat = get_object_or_404(Chat, id=idChat)
        messages = get_list_or_404(Message, chat=chat)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

