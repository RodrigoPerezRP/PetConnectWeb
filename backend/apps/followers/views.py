from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Follower
from apps.user.models import User
from .serializers import FollowerSerializer, GetUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 


class CreateFollow(APIView):
    def post(self,request,**kwargs):
        
        data = request.data 
        serializer = FollowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class ListFollowsUser(APIView):
    def get(self,request,**kwargs):
        username = kwargs.get('username')

        followers = get_list_or_404(Follower, user_r__username=username)
        serializer = GetUserSerializer(followers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UnFollowUser(APIView):
    def delete(self,request,**kwargs):
        id_follow = kwargs.get('id')
        follow = get_object_or_404(Follower, id=id_follow)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
