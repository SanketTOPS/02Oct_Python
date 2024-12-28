from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request): #Login Page
    return render(request,'index.html')

def signup(request): #Signup Page
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
        else:
            print(newuser.errors)
    return render(request,'signup.html')