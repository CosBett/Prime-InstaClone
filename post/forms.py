
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_profile, Post, Comment

# Account creation form. 
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_lenght=300, help_text= 'Required. Input a valid email address')
    
    class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')


class Update_profileForm(forms.ModelForm):

    class Meta:
      model = User_profile
      fields = ('name', 'profile_picture', 'bio', 'location')

class Update_UserForm(forms.ModelForm):
    email = forms.EmailField(max_lenght=300, help_text= 'Required. Input a valid email address')
    
    class Meta:
      model = User
      fields = ('username', 'email')

class PostForm(forms.ModelForm):
  
    class Meta:
        model = Post
        fields = ('image', 'caption')

