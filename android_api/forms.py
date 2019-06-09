from django import forms
from .models import User_Info

class Auth(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class Date(forms.Form):
    specdate = forms.CharField(max_length = 100)

    