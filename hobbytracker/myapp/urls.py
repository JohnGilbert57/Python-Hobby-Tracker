# Johnny Gilbert
# Ohio University
# how we call our functions and sets the URL routes
from django.urls import path
from .views import user_login_form, new_user_form
from . import views
urlpatterns = [
    path('task/', views.index, name = "index"),
    path('', views.user_login_form),
    path('createaccount/', views.new_user_form),
]