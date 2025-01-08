from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        if user: #TRUE
            print("Login Successfull!")
            request.session['user']=unm #session
            return redirect('notes')
        else:
            print("Error!Login Faild...")
            msg="Error!Login Faild..."
    return render(request,'index.html',{'msg':msg,'user':user})

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/')
        else:
            print(newuser.errors)
            msg="Error!Something went wrong...."
    return render(request,'signup.html',{'msg':msg})

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')