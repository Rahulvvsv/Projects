from django import forms
from django.forms import ModelForm
from wha_todo.models import *
from django.contrib.auth.models import User
from wha_todo.models import UserProfileInfo

class lists(forms.ModelForm):
    class Meta:
        model = work
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email','password')


class UserForm1(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('portfolio','profile_pic')
