from django import forms
from .models import HobbyUser

class UserForm(forms.ModelForm):
    class Meta:
        model = HobbyUser
        fields = [
            'firstName',
            'lastName',
            'userName',
            'password'
        ]