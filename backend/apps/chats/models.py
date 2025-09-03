from django.db import models
from apps.user.models import User
from django.utils import timezone

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_envia')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_recibe')
    date_created = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.chat.id}'