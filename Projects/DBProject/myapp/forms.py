from django import forms
from .models import *

class studData(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'

class updateData(forms.ModelForm):
    class Meta:
        model=studinfo
        fields=['name','email','city','dob','mobile']