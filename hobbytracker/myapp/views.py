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
from django.utils import timezone

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

def hobby_time_form(response):
    if response.method == "POST":
        form = HobbyTimeForm(response.POST)
        if(form.is_valid()):
            hobbyid = response.GET.get("hobby")
            times = []
            times.append(form.cleaned_data['sunTime'])
            times.append(form.cleaned_data['monTime'])
            times.append(form.cleaned_data['tueTime'])
            times.append(form.cleaned_data['wedTime'])
            times.append(form.cleaned_data['thuTime'])
            times.append(form.cleaned_data['friTime'])
            times.append(form.cleaned_data['satTime'])

            weekday = int(datetime.datetime.today().strftime('%w'))
            deltas = []
            for t in times:
                deltas.append(datetime.timedelta(minutes=t))

            i = 0
            now = timezone.now()
            for d in deltas:
                day_offset = datetime.timedelta(days=(i - weekday))
                end = now + day_offset
                start = end - d
                obj = HobbyTime(startTime=start,endTime=end)
                obj.hobbyUser = User.objects.get(pk=response.user.id)
                obj.hobby = Hobby.objects.get(pk=hobbyid)
                obj.save()
                i += 1
            return redirect("/hobbyview?hobbyid=" + hobbyid)
    else:
        form = HobbyTimeForm()
    return render(response, './myhobby/hobby_time.html', {'form': form})

def hobbiespage(response):

    if response.method == "POST":
        form = NewHobbyForm(response.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.hobbyUser = User.objects.get(pk=response.user.id)
            obj.save()
            return redirect("/userhobbies")
    else:
        form = NewHobbyForm()
    if response.user.is_anonymous:
        return redirect('/login')

    if response.method == "POST" and 'delete' in response.POST:
        delete_key = response.POST.get('delete')
        if Hobby.objects.filter(pk=delete_key).count() > 0:
            target = Hobby.objects.get(pk=delete_key)
            target.delete()

    # Get all hobbies for current user
    userHobbies = Hobby.objects.filter(hobbyUser=response.user)
    context = {
        'userHobbies': list(userHobbies),
        'form': form
        
    }
    return render(response, './myhobby/userhobbies.html', context)

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
        times_raw = HobbyTime.objects.raw('SELECT id,SUM((julianday(endTime) - julianday(startTime)) * 24 * 60) totalmins,date(endTime) hobbydate FROM myapp_hobbytime WHERE hobby_id='+ str(hobby.id) +' AND startTime>=date(\'now\',\'-'+ str(days_back) +' day\') AND endTime<=date(\'now\',\''+ str(7 - days_back) +' day\') GROUP BY date(startTime)')
	
        times = []
        # Create the float values for the chart
        for t in times_raw:
            times.append(round(t.totalmins,2))

        labels = []
        # Create the labels for the chart
        for t in times_raw:
            labels.append(datetime.datetime.strptime(t.hobbydate,'%Y-%m-%d').date().strftime('%A %B %-d'))

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
        if(percentDifference < 45.0):
            # append happy to basepath
            # print("Happy")
            basepath = basepath + ("_happy.gif")
        elif (percentDifference >= 45.0 and percentDifference < 75.0):
            # append content to basepath
            # print("Content")
            basepath = basepath + ("_content.gif")
        elif (percentDifference >= 75.0 and percentDifference < 100):
           # print("Sad")
            basepath = basepath + ("_sad.gif")
            # append the sad
        else:
            basepath = basepath + ("_content.gif")
        # Use the below for the HTMLs
        context["fullName"] = basepath
        context["hobby"] = hobby
        context["qs"] = labels
        context["vals"] = times
        return context
    
