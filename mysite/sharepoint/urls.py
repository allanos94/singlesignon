from django.contrib import admin
from django.urls import path
from sharepoint import views

urlpatterns = [
    path('challenge', views.view_challenge, name="view_challenge"),
    path('addidea', views.add_idea, name="add_idea"),
    path('idea', views.view_idea, name="view_idea"),
]
