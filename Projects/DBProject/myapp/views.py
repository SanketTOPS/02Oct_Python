from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        stdata=studData(request.POST)
        if stdata.is_valid():
            stdata.save()
            print("Data inserted!")
        else:
            print(stdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    print("Current ID:",stid)
    if request.method=='POST':
        updReq=updateData(request.POST,instance=stid)
        if updReq.is_valid():
            updReq.save()
            print("Update Successfully!")
            return redirect('showdata')
        else:
            print(updReq.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')
    