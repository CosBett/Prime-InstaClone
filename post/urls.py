from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'landing_page' ),
    path('signup/',views.sign_up, name = 'signup' ),

]