from django.db import models
from apps.user.models import User 

class Notification(models.Model):
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    reason = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.reason} - {self.user_receiver.username}'