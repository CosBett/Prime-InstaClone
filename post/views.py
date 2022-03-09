from django.shortcuts import render,redirect
from .forms import SignupForm, Update_profileForm, Update_UserForm, PostForm, CommentForm
from .models import User_profile,Post, Comment, Follow
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    
    return render(request, 'landing_page/landing_page.html') 

# view function for account creation.    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_date.get('password1')
            user = authenticate(username=username, password= raw_password)
            login(request, user)
            
            return redirect(index)
    else :
        form = SignupForm()

    landing_context = {'form': form}    
    
    return render(request, 'landing_page/landing_page.html', landing_context) 

