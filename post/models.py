from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(upload_to='pictures/', default='default.png')
    bio = models.TextField(max_length=1500, default="My Bio", blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} User_profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User_profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user  

    def delete_profile(self):
        self.delete()  

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    

class Post(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    caption = models.CharField(max_length=500, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True,)

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Post'

    