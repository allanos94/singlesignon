from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name="index"),
    path(
        r'<int:poll_id>/answers/<int:answer_id>/edit',
        views.edit_answer,
        name="edit_answer",
    ),
    path('myprofile', views.my_profile, name="my_profile")
]
