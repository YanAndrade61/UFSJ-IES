from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def galery(request):
    return render(request,'galery.html')

def workshop(request):
    return render(request,'workshop.html')

def login(request):
    return render(request,'login.html')