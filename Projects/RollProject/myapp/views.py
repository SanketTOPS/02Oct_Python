from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def index(request):
    if request.method == "POST":
        roll = request.POST["roll"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]

        user = usersignup.objects.filter(roll=roll, email=email, mobile=mobile)
        if user:
            print("Login Successfully!")
            request.session["roll"] = roll
            return redirect("home")
        else:
            print("Error!")
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        newuser = signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect("/")
        else:
            print(newuser.errors)
    return render(request, "signup.html")


def home(request):
    roll = request.session.get("roll")
    return render(request, "home.html", {"roll": roll})
