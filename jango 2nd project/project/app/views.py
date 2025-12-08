from django.shortcuts import render
def landing(req):
    return render(req,'landing.html')
def home(req):
    return render(req,"home.html")
    

# Create your views here.
