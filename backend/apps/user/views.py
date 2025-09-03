from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .models import User 
from .serializers import RegisterSerializer, ListSerializer

class CreateUser(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListUsers(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = ListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetUser(APIView):
    def get(self,request, **kwargs):
        slug = kwargs.get('slug')
        user = get_object_or_404(User, slug=slug)
        serializer = ListSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
