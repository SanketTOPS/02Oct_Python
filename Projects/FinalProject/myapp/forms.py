from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','state','city','mobile']

class notesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'
