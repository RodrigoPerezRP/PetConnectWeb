from django.shortcuts import get_list_or_404, get_object_or_404
from apps.user.models import User 
from .models import Notification

from .serializers import NotificationSerializer, GetInfoUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateNotification(APIView):
    def post(self,request,**kwargs):
        data = request.data
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListNotificationsForUser(APIView):
    def get(self,request,**kwargs):
        id_user = kwargs.get('id')
        notifications = get_list_or_404(Notification, user_receiver__id=id_user)
        serializer = GetInfoUserSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

