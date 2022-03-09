from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'landing_page/landing_page.html') 
# view function for account creation.    
def sign_up(request):
    return render(request, 'landing_page/landing_page.html') 

        