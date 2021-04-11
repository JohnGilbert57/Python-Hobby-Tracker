"""serves our urls to the browser"""

# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# how we call our functions and sets the URL routes
from django.urls import path, include
from . import views
from .views import new_user_form, hobbiespage, HobbyChartView, hobby_time_form

urlpatterns = [
    path('', views.baseUrl),
    path('', include("django.contrib.auth.urls")),
    path('createaccount/', new_user_form, name = "register"),
    path('userhobbies/', hobbiespage),
    path('hobbyview/', HobbyChartView.as_view(), name='home'),
    path('hobbyview/addtime', hobby_time_form, name = 'addtime')
]
