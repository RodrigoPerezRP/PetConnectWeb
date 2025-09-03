from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

from .serializers import CommentSerializer
from .models import Comment

class ListCommentsPost(APIView):
    def get(self,request,**kwargs):
        id_post = kwargs.get('id')
        comments = get_list_or_404(Comment, post__id=id_post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateComment(APIView):
    def post(self,request):
        data = request.data
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EditComment(APIView):
    def patch(self,request,**kwargs):
        data = request.data
        id_comment = kwargs.get('id')
        comment = get_object_or_404(Comment, id=id_comment)
        serializer = CommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteComment(APIView):
    def delete(self,request,**kwargs):
        id_comment = kwargs.get('id')
        comment = get_object_or_404(Comment, id=id_comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)