from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from polls import models
from polls.forms.user import ProfileForm

@login_required
def index(request):
    return render(request, 'polls/index.html', {})

@login_required
def my_profile(request):
    current_user_profile = request.user.profile
    user_form = models.ProfileForm.objects.get(site=current_user_profile.site)
    fields = user_form.form_fields['fields']
    form = ProfileForm(fields=fields, initial=current_user_profile.dynamic_fields)
    return render(request, 'polls/current_user.html', {'form': form})
