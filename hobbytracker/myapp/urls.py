# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# how we call our functions and sets the URL routes
from django.contrib import admin
from django.urls import path, include
from .views import new_user_form, hobbiespage, baseUrl, HobbyChartView
from . import views
urlpatterns = [
    path('userhobbies/task/', views.task, name = "index"),
    path('', views.baseUrl),
    path('', include("django.contrib.auth.urls")),
    path('createaccount/', views.new_user_form, name = "register"),
    path('userhobbies/', views.hobbiespage),
    path('test/', views.HobbyChartView.as_view(), name='home'),
    path('sprites/', views.sprites),
    
]
