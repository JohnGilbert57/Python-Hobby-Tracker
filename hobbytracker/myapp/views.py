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
    if response.method == "POST" and 'deleteuser' in response.POST:
        username = response.user.username
        u = User.objects.get(username = username)
        u.delete()
        return redirect('/login')
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
        times_raw = HobbyTime.objects.raw('SELECT id,SUM((julianday(endTime) - julianday(startTime)) * 24 * 60) totalmins,date(endTime) hobbydate FROM myapp_hobbytime WHERE hobby_id='+ str(hobby.id) +' AND startTime>=date(\'now\',\'-'+ str(days_back) +' day\') AND endTime<=date(\'now\',\''+ str(7 - days_back) +' day\') GROUP BY date(startTime)')
	
        times = []
        # Create the float values for the chart
        for t in times_raw:
            times.append(round(t.totalmins,2))

        labels = []
        # Create the labels for the chart
        for t in times_raw:
            labels.append(datetime.datetime.strptime(t.hobbydate,'%Y-%m-%d').date().strftime('%A, %B %-d'))
        
        # Gets first nonzero time logged from db
        first_time_raw = HobbyTime.objects.raw('SELECT id,date(startTime) startdate FROM myapp_hobbytime WHERE hobby_id='+str(hobby.id)+' AND (julianday(endTime) - julianday(startTime))*24*60 > 0  ORDER BY startTime LIMIT 1')

        first_time_str = "" 
        for f in first_time_raw:
             first_time_str = f.startdate


        # Using a simple path that will be the first half of the name of the sprite (e.g. Rufus)
        basepath = hobby.spriteId.imageName

        weekly_percent = 50

        # If the user has logged time
        if(first_time_str != ""):
            first_time = datetime.datetime.strptime(first_time_str, '%Y-%m-%d')
        
            todays_date = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            day_offset = datetime.timedelta(days=(days_back))
            sunday_date = todays_date - day_offset
            
            days_in_period = days_back + 1 

            # if the user begam their hobby after sunday of this week
            if(first_time > sunday_date):
                days_in_period = days_in_period - (first_time - sunday_date).total_seconds()/86400
        
         
            # Find the target time total that the user should have for their hobby
            target_daily_time = hobby.timeLimit/7

            daily_percentages = []
            i = 0
            for t in times:
                # Prevent future dates from being added to total
                if(target_daily_time > 0 and i <= days_back):
                    daily_percentages.append(t/target_daily_time*100)
                else:
                    daily_percentages.append(0)
                i += 1
            
            total_percentage = 0
            for d in daily_percentages:
                total_percentage = total_percentage + d

            weekly_percent = total_percentage/days_in_period
            
        
        # Choose pet met
        if(weekly_percent >= 75.0):
            # append happy to basepath
            # print("Happy")
            basepath = basepath + ("_happy.gif")
        elif (weekly_percent >= 45.0 and weekly_percent < 75.0):
            # append content to basepath
            # print("Content")
            basepath = basepath + ("_content.gif")
        elif (weekly_percent > 0.0 and weekly_percent < 45.0):
            # print("Sad")
            basepath = basepath + ("_sad.gif")
            # append the sad
        else:
            basepath = basepath + ("_content.gif")
        totalMinutes = 0
        for i in times:
            totalMinutes = totalMinutes + i
        if(totalMinutes >= hobby.timeLimit):
            totalMinutes = hobby.timeLimit
        # Use the below for the HTMLs
        context["timeLog"] = hobby.timeLimit - totalMinutes
        context["fullName"] = basepath
        context["hobby"] = hobby
        context["qs"] = labels
        context["vals"] = times
        return context
    
