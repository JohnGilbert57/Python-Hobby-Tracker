# Johnny Gilbert
# Ohio University
# displays the UI for the application
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import UserLoginForm, NewUserForm
from .models import HobbyUser
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import *

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    return render(request, './myhobby/index.html')
def user_login_form(request):
    form = UserLoginForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect(index)
    context = {
        'form': form
    }
    return render(request, './registration/login.html', context)
def new_user_form(response):
    if response.method == "POST":
        form = NewUserForm(response.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/login')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(response, './myhobby/new_user.html', context)
def hobbiespage(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, './myhobby/userhobbies.html')
def baseUrl(response):
    return redirect('/login')

