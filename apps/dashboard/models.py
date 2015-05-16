from django.contrib.auth.models import User
from django.db import models

class R:

    def __init__(self, status=200, message='', errors='', data={}):
        self.status = status
        self.message = message
        self.errors = errors
        self.data = data

    def get_object(self):
        result = {}
        if self.status:
            result['status'] = self.status
        if self.message:
            result['message'] = self.message
        if self.errors:
            result['errors'] = self.errors
        if self.data:
            result['data'] = self.data
        return result

class Post(models.Model):
    user = models.OneToOneField(User, related_name='posts')
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='postimages/', null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
