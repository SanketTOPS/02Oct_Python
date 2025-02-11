from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view



def index(request):
    return render(request,'index.html')

@api_view(["GET"])
def getall(request):
    stdata = studinfo.objects.all()
    serial = studSerializer(stdata, many=True)
    return Response(data=serial.data)
