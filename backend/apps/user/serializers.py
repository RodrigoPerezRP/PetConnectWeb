from rest_framework import serializers

from .models import User 

class RegisterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['email', 'username', 'last_name', 'password', 'slug']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                'id',
                'email',
                'description',
                'slug',
                'avatar',
                'username',
                'last_name',
                'phone_number',]