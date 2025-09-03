from django.db import models
from apps.user.models import User 
from apps.posts.models import Post 


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_sender")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content}'