from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.landing_page, name = 'landing_page' ),
    path('signup/',views.sign_up, name = 'signup' ),
    path('home/',views.index, name = 'homepage' ),
    path('account/', include('django.contrib.auth.urls')),
    path('userprofile/<username>/', views.user_profile, name='userprofile'),
    path('profile/<username>/',views.profile, name='profile'),
    path('post/<id>', views.post_comments, name='comment'),
    path('search/', views.search_profile, name='search'),
    path('likes', views.like_post, name='likes'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
]

