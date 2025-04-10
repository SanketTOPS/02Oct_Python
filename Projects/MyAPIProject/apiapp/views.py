from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getall(requset):
    stdata=studinfo.objects.all()
    serial=studSerial(stdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def getstid(requset,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=studSerial(stid)
    return Response(data=serial.data)

@api_view(['GET','DELETE'])
def deletestid(requset,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if requset.method=="GET":
        serial=studSerial(stid)
        return Response(data=serial.data)
    if requset.method=='DELETE':
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        newdata=studSerial(data=request.data)
        if newdata.is_valid():
            newdata.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)