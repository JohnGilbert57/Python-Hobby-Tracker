# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from .models import HobbyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = HobbyUser
        fields = [
            'userName',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
        labels ={
            'userName': 'Username',
            'password': 'Password'
        }
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'userName': 'Username',
            'password': 'Password'
        }