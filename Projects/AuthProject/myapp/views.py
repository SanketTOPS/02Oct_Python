from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request): #Login Page
    msg=""
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session['user']=unm #create a session
            return redirect('home')
        else:
            print("Error!Login faild...")
            msg="Login faild..."
    return render(request,'index.html',{'msg':msg})

def signup(request): #Signup Page
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            msg="Signup Successfully!"
            return redirect('/')
        else:
            print(newuser.errors)
            msg="Something went wrong..."
    return render(request,'signup.html',{'msg':msg})

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
