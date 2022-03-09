import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_profile, Post, Comment

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_lenght=300, help_text= 'Required. Inform a valid email address'),
    class Meta:
      model = User
      fields = 