from .models import Follower
from rest_framework import serializers
from apps.user.models import User

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

class GetInfoUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'slug',
            'username',
            'last_name',
        ]

class GetUserSerializer(serializers.ModelSerializer):
    user_s = GetInfoUser()
    user = user_s

    class Meta:
        model = Follower 
        fields = ['user_s', 'user']