import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from google import models
from django.conf import settings
from django.urls import reverse

def index(request):
    template = loader.get_template('google/index.html')
    context = {
        'logged_in': False,
    }
    return HttpResponse(template.render(context, request))
