from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from .forms import SignupForm, Update_profileForm, Update_UserForm, PostForm, CommentForm
from .models import User_profile,Post, Comment, Follow
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib import messages



# View function for homepage and login 

def landing_page(request):
  
     return render(request,'landing_page/landing_page.html') 

def log_in(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('login')
    else:
		    return render(request, 'registration/login.html', {})

@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    print('IMG', images)
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
    index_context = {'images': images,'form': form,'users': users}

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
            
            return redirect('homepage')
    else :
        form = SignupForm()

    landing_context = {'form': form}    
    
    return render(request, 'registration/signup.html', landing_context) 

login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        userform = Update_profileForm(request.POST, instance=request.user)
        profileform = Update_UserForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
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

@login_required(login_url='login')
def post_comments(request, id):
    image = get_object_or_404(Post, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    comments_context= {'image': image,'form': form, 'is_liked': is_liked,'total_likes': image.total_likes()
    }
    return render(request, 'comments_post.html', comments_context)

def like_post(request):
    image = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = False
    liked_context = {'image': image,'is_liked': is_liked,'total_likes': image.total_likes()
    }
    if request.is_ajax():
        html = render_to_string('likes.html', liked_context, request=request)
        return JsonResponse({'form': html})
        

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = User_profile.search_profile(name)
        message = f'name'
        search_context= { 'results': results, 'message': message }
        return render(request, 'search.html', search_context)
    else:
        message = "Please search for a valid username"
    return render(request, 'search.html',{'message': message})

def follow(request, to_follow):
    if request.method == 'GET':
        userprofile = User_profile.objects.get(pk=to_follow)
        followers = Follow(follower=request.user.profile, followed=userprofile)
        followers.save()

        return redirect('userprofile', userprofile.user.username)

def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile = User_profile.objects.get(pk=to_unfollow)
        unfollow = Follow.objects.filter(follower=request.user.profile, followed=user_profile)
        unfollow.delete()
        return redirect('userprofile', user_profile.user.username)

def logout_view(request):
    logout(request)
    return redirect('landing_page')
