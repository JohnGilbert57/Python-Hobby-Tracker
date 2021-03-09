# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# displays the UI for the application
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import NewUserForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import *
from django.views.generic import TemplateView
from .models import Hobby

# Create your views here.
def task(request):
    #return HttpResponse("Hello World")
    return render(request, './myhobby/task.html')

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
class HobbyChartView(TemplateView):
    template_name = './myhobby/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Hobby.objects.all()
        return context
def sprites(request):
    return render(request, './myhobby/sprites.html')