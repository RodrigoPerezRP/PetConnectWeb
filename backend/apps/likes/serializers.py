from rest_framework import serializers
from .models import Like
from apps.user.models import User 
from apps.posts.models import Post

class InfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'slug',
            'username',
            'last_name',
        ]

class InfoPost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']

class LikeSerializer(serializers.ModelSerializer):
    user = InfoUserSerializer()
    post = InfoPost()
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'date_created']

class CreataLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'