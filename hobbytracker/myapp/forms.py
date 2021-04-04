# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from .models import Hobby, HobbyTime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class HobbyTimeForm(forms.Form):
    timeSpent = forms.IntegerField(label='Time Spent')

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
            'timeLimit': 'Goal (0.0-168.0 Hours)'
        }

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            'username': 'Username',
        }
# class TimeForm(models.ModelForm):

