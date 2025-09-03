from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from .serializers import LikeSerializer, CreataLikeSerializer
from .models import Like

class ListLikeForPost(APIView):
    def get(self,request,**kwargs):
        id_post = kwargs.get('id')
        likes = get_list_or_404(Like, post__id=id_post)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateLike(APIView):
    def post(self,request):

        data = request.data 

        data = {
            'post': data['idPost'],
            'user': data['idUser'],
        }

        serializer = CreataLikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLike(APIView):
    def delete(self,request,**kwargs):
        id = kwargs.get('id')
        id_like = get_object_or_404(Like, id=id)
        id_like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
