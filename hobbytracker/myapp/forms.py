# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from .models import Hobby
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django_popup_view_field.fields import PopupViewField

class NewHobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'name',
            'spriteId',
            'timeLimit'
        ]
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'spriteId': forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'name': 'Hobby Name',
            'spriteId': 'Sprite Figure',
            'timeLimit': 'Goal'
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
