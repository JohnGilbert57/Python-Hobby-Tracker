# Johnny Gilbert
# Ohio University
# how we call our functions and sets the URL routes
from django.contrib import admin
from django.urls import path, include
from .views import user_login_form, new_user_form, hobbiespage
from . import views
urlpatterns = [
    path('userhobbies/task/', views.index, name = "index"),
    path('', include("django.contrib.auth.urls")),
    path('createaccount/', views.new_user_form, name = "register"),
    path('userhobbies/', views.hobbiespage)
]