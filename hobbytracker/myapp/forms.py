# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from .models import Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class NewHobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'name',
            'spriteId',
            'timeLimit'
        ]
        labels = {
            'name': 'Hobby Name',
            'spriteId': 'Sprite Figure',
            'timeLimit': 'Goal'
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
