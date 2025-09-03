from rest_framework import serializers
from .models import Notification
from apps.user.models import User

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class GetInfoUserSerializer(serializers.ModelSerializer):
    user_sender = UserSerializer()
    user_receiver = UserSerializer()
    class Meta:
        model = Notification
        fields = [
'id',
'user_sender',
'user_receiver',
'reason',

        ]