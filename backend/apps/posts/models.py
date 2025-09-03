from django.db import models
from apps.user.models import User

class Post(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'