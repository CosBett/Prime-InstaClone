from django.shortcuts import render

# Create your views here.
def index(request):
    landing_page = landing_page
    return render(request, 'landing_page.html', landing_page) 
