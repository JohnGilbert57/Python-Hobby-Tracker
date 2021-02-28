# Johnny Gilbert
# Nathaniel Buchanan
# Ohio University
# how we call our functions and sets the URL routes
from django.urls import path
from .views import user_login_form, new_user_form, HobbyChartView
from . import views
urlpatterns = [
    path('task/', views.index, name = "index"),
    path('', views.user_login_form),
    path('test/', views.HobbyChartView.as_view(), name='home'),
    path('createaccount/', views.new_user_form),
]