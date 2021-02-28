# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# displays the UI for the application

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import UserLoginForm, NewUserForm
from .models import HobbyUser
from django.shortcuts import redirect
#from django.views import generic
from django.views.generic import TemplateView
from .models import Hobby


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




class HobbyChartView(TemplateView):
    template_name = './myhobby/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Hobby.objects.all()
        return context