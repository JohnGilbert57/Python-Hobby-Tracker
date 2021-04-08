# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# displays the UI for the application
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import NewUserForm, NewHobbyForm, HobbyTimeForm
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import *
from django.views.generic import TemplateView
from .models import Hobby,HobbyTime
from django.contrib.auth.models import User
import datetime

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

def hobby_time_form(response):
    if response.method == "POST":
        form = HobbyTimeForm(response.POST)
        if(form.is_valid()):
            hobbyid = response.GET.get("hobby")
            time_int = form.cleaned_data['timeSpent']
            delta = datetime.timedelta(minutes=time_int)
            end = datetime.datetime.now()
            start = end - delta
            obj = HobbyTime(startTime=start,endTime=end)
            obj.hobbyUser = User.objects.get(pk=response.user.id)
            obj.hobby = Hobby.objects.get(pk=hobbyid)
            obj.save()
            return redirect("/hobbyview?hobbyid=" + hobbyid)
    else:
        form = HobbyTimeForm()
    return render(response, './myhobby/hobby_time.html', {'form': form})

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

# Class used for Chart/Sprite
class HobbyChartView(TemplateView):
    template_name = './myhobby/chart.html'
    # Used for the chart information and sprite information
    def get_context_data(self, **kwargs):
        # Use the below for the context information for database
        context = super().get_context_data(**kwargs)
        hobbyid = self.request.GET.get('hobbyid')
        hobby = Hobby.objects.get(pk=hobbyid)
        
        # Days_back is the number of days prior to today that will be included on graph
        days_back = int(datetime.datetime.today().strftime('%w'))
        
        # Gets an array of times that will go back x number of days
        # (I could not get a format string to work properly)
        times_raw = HobbyTime.objects.raw('SELECT id,SUM((julianday(endTime) - julianday(startTime)) * 24 * 60) totalmins,date(endTime) hobbydate FROM myapp_hobbytime WHERE hobby_id='+ str(hobby.id) +' AND startTime>=date(\'now\',\'-'+ str(days_back) +' day\') GROUP BY date(startTime)')
	
        times = []
        # Create the float values for the chart
        for t in times_raw:
            times.append(round(t.totalmins,2))

        labels = []
        # Create the labels for the chart (temp for now)
        for t in times_raw:
            labels.append(t.hobbydate)

        # This will get the total amount of mintutes the user has done
        totalMinutes = 0
        for i in times:
            totalMinutes = totalMinutes + i

        # Find the target time total that the user should have for their hobby
        targetTimeTotal = hobby.timeLimit * (days_back + 1)

        percentDifference = (float(targetTimeTotal - totalMinutes)) / float(targetTimeTotal) * 100.0

        # Consider days in period, number in days in period * controlLimit (percentages)
        # Compare to a percentage value

        # Using a simple path that will be the first half of the name of the sprite (e.g. Rufus)
        basepath = hobby.spriteId.imageName
        
        # Choose pet met
        if(percentDifference >= 75.0):
            # append happy to basepath
            # print("Happy")
            basepath = basepath + ("_happy.gif")
        elif (percentDifference >= 45.0 and percentDifference < 75.0):
            # append content to basepath
            # print("Content")
            basepath = basepath + ("_content.gif")
        elif (percentDifference < 45.0):
           # print("Sad")
            basepath = basepath + ("_sad.gif")
            # append the sad
        else:
            basepath = basepath + ("_content.gif")


        # Use the below for the HTML
        context["fullName"] = basepath
        context["hobby"] = hobby
        context["qs"] = labels
        context["vals"] = times
        return context
