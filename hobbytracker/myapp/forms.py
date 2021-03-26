# Johnny Gilbert
# Ohio University
# the format for the user login; creates the objects basesd upon the models and sets the data
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# class HobbyList(forms.ModelForm):
#     class Meta:
#         model = Hobby
#         fields = [
#             'hobby',
#             'goal'
#         ]
#         labels = {
#             'hobby': 'Hobby',
#             'goal': 'Goal'
#         }


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
