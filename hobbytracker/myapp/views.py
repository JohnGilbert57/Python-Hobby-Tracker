# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# displays the UI for the application
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import NewUserForm, NewHobbyForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import *
from django.views.generic import TemplateView
from .models import Hobby,HobbyTime
from django.contrib.auth.models import User

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

def new_hobby_form(response):
    if response.method == "POST":
        form = NewHobbyForm(response.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.hobbyUser = User.objects.get(pk=response.user.id)
            obj.save()
            return redirect("/userhobbies")
    else:
        form = NewHobbyForm()
    return render(response, './myhobby/new_hobby.html', {'form': form})

def hobbiespage(request):
    if request.user.is_anonymous:
        return redirect('/login')

    if request.method == "POST" and 'delete' in request.POST:
        print(request.POST.get('delete'))
        delete_key = request.POST.get('delete')
        if Hobby.objects.filter(pk=delete_key).count() > 0:
            target = Hobby.objects.get(pk=delete_key)
            target.delete()

    # Get all hobbies for current user
    userHobbies = Hobby.objects.filter(hobbyUser=request.user)
    context = {
        'userHobbies': list(userHobbies),
    }
    return render(request, './myhobby/userhobbies.html', context)

def baseUrl(response):
    return redirect('/login')

class HobbyChartView(TemplateView):
    template_name = './myhobby/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hobbyid = self.request.GET.get('hobbyid')
        hobby = Hobby.objects.get(pk=hobbyid)
        times = list(HobbyTime.objects.filter(hobby=hobby))
        labels = []
        for t in times:
            labels.append(t.startTime.date())
        vals = []
        for t in times:
            vals.append((t.endTime - t.startTime).total_seconds() / 60.0)
        context["hobby"] = hobby
        context["qs"] = labels
        context["vals"] = vals
        return context
























