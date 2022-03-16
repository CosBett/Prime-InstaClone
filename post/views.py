from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import SignupForm, Update_profileForm, Update_UserForm, PostForm, CommentForm
from .models import User_profile,Post, Comment, Follow
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# View function for homepage and login 

def landing_page(request):
  
     return render(request,'landing_page/landing_page.html') 

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('homepage')
       
    else:
        return redirect('login')
        
@login_required(login_url='login')
def index(request):
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    index_context = {'posts': posts,'form': form,'users': users}

    return render(request, 'index.html', index_context)

# view function for account creation.    
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password= raw_password)
            login(request, user)
            
            return redirect('login')
    else :
        form = SignupForm()

    landing_context = {'form': form}    
    
    return render(request, 'registration/signup.html', landing_context) 

