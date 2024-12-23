from django import forms
from .models import *

class studData(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'