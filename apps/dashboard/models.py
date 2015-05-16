from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user = models.OneToOneField(User, related_name='posts')
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='postimages/', null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
