from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = ThumbnailerImageField(resize_source={'size': (300, 300), 'crop': 'smart'}, upload_to='userProfile/', default='default.jpg')

    def __str__(self):
        return f'Profile of {self.user.username}'
