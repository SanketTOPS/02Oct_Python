from django.contrib import admin
from .models import *

# Register your models here.

class studData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','city','mobile','email','dob','address']

admin.site.register(studinfo,studData)