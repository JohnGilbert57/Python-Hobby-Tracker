from django.urls import path
from .views import new_user_form
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('create/', views.new_user_form)
]