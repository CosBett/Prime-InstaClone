from django.contrib import admin
from .models import User_profile, Post, Comment, Follow
# Register your models here.

admin.site.register(User_profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)