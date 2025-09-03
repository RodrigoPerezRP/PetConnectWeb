from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import PostSerializer

from apps.user.models import User 
from .models import Post

class ListAllPost(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreatePost(APIView):
    def post(self,request,**kwargs):
        data = request.data 
        data['is_public'] = True
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditPost(APIView):
    def patch(self,request,**kwargs):
        data = request.data
        id_post = kwargs.get('id')
        post = get_object_or_404(Post, id=id_post)

        old_serializer = PostSerializer(post)

        serializer = PostSerializer(post, data=data, partial=True)
        if serializer.is_valid():
            if serializer.data != old_serializer.data:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeletePost(APIView):
    def delete(self,**kwargs):
        id = kwargs.get('id')
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListPostsForUser(APIView):
    def get(self,request,**kwargs):
        id = kwargs.get('id')
        posts = get_list_or_404(Post, user__id=id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 