from django.db import models
from apps.user.models import User 


class Follower(models.Model):
    user_s = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_s")
    user_r = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_r")

    class Meta:
        def __str__(self):
            return f'{self.user_s.username}'