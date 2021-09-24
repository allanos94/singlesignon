from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name="index"),
    path('myprofile', views.my_profile, name="my_profile")
]
