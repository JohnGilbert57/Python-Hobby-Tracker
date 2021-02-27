from django import forms
from .models import HobbyUser

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
class NewUserForm(forms.ModelForm):
    class Meta:
        model = HobbyUser
        fields = [
            'firstName',
            'lastName',
            'userName',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
        labels ={
            'firstName': 'First Name', 
            'lastName': 'Last Name',
            'userName': 'Username',
            'password': 'Password'

        }