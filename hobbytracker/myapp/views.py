from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import UserLoginForm, NewUserForm
from .models import HobbyUser
from django.shortcuts import redirect
from django.views import generic
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
    return render(request, './myhobby/user_login.html', context)
def new_user_form(request):
    form = NewUserForm(request.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect(index)
    context = {
        'form': form
    }
    return render(request, './myhobby/new_user.html', context)

