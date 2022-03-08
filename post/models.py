from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(upload_to='pictures/', default='default.png')
    bio = models.TextField(max_length=1500, default="My Bio", blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} User_profile'
