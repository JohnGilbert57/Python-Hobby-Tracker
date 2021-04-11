"""Created forms that will be called to pass forms to the html"""
# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Hobby

class HobbyTimeForm(forms.Form):
    """adding time to a hobby form"""
    sunTime = forms.FloatField(label='Sunday',initial=0)
    monTime = forms.FloatField(label='Monday',initial=0)
    tueTime = forms.FloatField(label='Tuesday',initial=0)
    wedTime = forms.FloatField(label='Wednesday',initial=0)
    thuTime = forms.FloatField(label='Thursday',initial=0)
    friTime = forms.FloatField(label='Friday',initial=0)
    satTime = forms.FloatField(label='Saturday',initial=0)

class NewHobbyForm(forms.ModelForm):
    """creating a new hobby"""
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
            'timeLimit': 'Goal (0.0-168.0 Hours)'
        }

class NewUserForm(UserCreationForm):
    """login form"""
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            'username': 'Username',
        }
        