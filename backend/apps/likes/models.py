from django.db import models
from apps.posts.models import Post 
from apps.user.models import User 

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title} - Dueño: {self.post.user.username}'