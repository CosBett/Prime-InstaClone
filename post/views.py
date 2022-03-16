from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
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

login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = Update_profileForm(request.POST, instance=request.user)
        prof_form = Update_UserForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and prof_form.is_valid():
            userform.save()
            profileform.save()
            return HttpResponseRedirect(request.path_info)
    else:
        userform = Update_profileForm(instance=request.user)
        profileform = Update_UserForm(instance=request.user.profile)
        
    profile_context = {'userform': userform,'profileform': profileform,'images': images }
    return render(request, 'profile.html', profile_context)

login_required(login_url='login')
def user_profile(request, username):
    userprofile = get_object_or_404(User, username=username)
    if request.user == userprofile:
        return redirect('profile', username=request.user.username)
    user_posts = userprofile.profile.posts.all()
    
    followers = Follow.objects.filter(followed=userprofile.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    userprofile_context = { 'userprofile': userprofile, 'user_posts': user_posts, 'followers': followers, 'follow_status': follow_status }

    return render(request, 'userprofile.html', userprofile_context)