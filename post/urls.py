from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.landing_page, name = 'landing_page' ),
    path('signup/',views.sign_up, name = 'signup' ),
    path('account/', include('django.contrib.auth.urls')),


]