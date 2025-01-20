from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings


# Create your views here.
def index(request):
    msg = ""
    user = request.session.get("user")
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]

        user = userSignup.objects.filter(username=unm, password=pas)
        userid = userSignup.objects.get(username=unm)
        print("UserID:", userid.id)
        if user:  # TRUE
            print("Login Successfull!")
            request.session["user"] = unm  # session
            request.session["userid"] = userid.id
            return redirect("notes")
        else:
            print("Error!Login Faild...")
            msg = "Error!Login Faild..."
    return render(request, "index.html", {"msg": msg, "user": user})


def signup(request):
    msg = ""
    if request.method == "POST":
        newuser = signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect("/")
        else:
            print(newuser.errors)
            msg = "Error!Something went wrong...."
    return render(request, "signup.html", {"msg": msg})


def notes(request):
    msg = ""
    user = request.session.get("user")
    if request.method == "POST":
        newnote = notesForm(request.POST, request.FILES)
        if newnote.is_valid():
            newnote.save()
            print("Your notes has been submitted!")
            msg = "Your notes has been submitted!"
        else:
            print(newnote.errors)
            msg = "Error!Something went wrong..."
    return render(request, "notes.html", {"user": user, "msg": msg})


def profile(request):
    user = request.session.get("user")
    userid = request.session.get("userid")
    cid = userSignup.objects.get(id=userid)
    print("Current User ID:", cid)
    if request.method == "POST":
        updateReq = updateForm(request.POST, instance=cid)
        if updateReq.is_valid():
            updateReq.save()
            request.session.delete()
            return redirect("/")
        else:
            print(updateReq.errors)
            msg = "Error!Something went wrong...."
    return render(request, "profile.html", {"user": user, "cid": cid})


def about(request):
    user = request.session.get("user")
    return render(request, "about.html", {"user": user})


def contact(request):
    user = request.session.get("user")
    if request.method == "POST":
        newcontact = contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submitted!")

            # Email Sending Code
            send_mail(
                subject="Thankyou!",
                message=f"Hello User!\n\nThank you for connecting with us!\nWe will contact you.\n\n\Thanks & Regards!\nSanket Chauhan\n+91 9724799469 | sanket.tops@gmail.com",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    "meetladva1684@gmail.com",
                    "premahir610@gmail.com",
                    "harshitprajapati926@gmail.com",
                    "hemilpatel61024@gmail.com",
                    "garaniyachintan8@gmail.com",
                    "sohamparmar79@gmail.com",
                    "gokanipriyanshi@gmail.com",
                    "devangikachhadiya37@gmail.com",
                    "ruchipandya20@gmail.com",
                ],
            )

        else:
            print(newcontact.errors)
    return render(request, "contact.html", {"user": user})


def userlogout(request):
    logout(request)
    return redirect("/")
