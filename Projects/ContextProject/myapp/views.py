from django.shortcuts import render
import random

# Create your views here.
def index(request):
    name="Ashok"
    return render(request,'index.html',{'nm':name})

def about(request):
    num=random.randint(1111,9999)
    return render(request,'about.html',{'num':num})

n=1
def contact(request):
    global n
    n+=1
    return render(request,'contact.html',{'n':n})