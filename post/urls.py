from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.landing_page, name = 'landing_page' ),
    path('signup/',views.sign_up, name = 'signup' ),
    path('home/',views.index, name = 'homepage' ),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('userprofile/<username>/', views.user_profile, name='userprofile'),
    path('profile/<username>/',views.profile, name='profile'),
    path('post/<id>', views.post_comments, name='comment'),

]