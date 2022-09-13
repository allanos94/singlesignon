from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
import requests
import os

def make_request(url, params):
    base_url = "https://public-api.wazoku.com/api/v4"
    token_value = os.environ.get("TOKEN_VALUE")
    headers = {
        "Authorization": f"Token {token_value}"
    }
    response = requests.get(
        url=f"{base_url}{url}",
        headers=headers,
        params=params,
    )

    assert response.status_code == 200, response

    return response.json()

# Create your views here.
@xframe_options_exempt
@csrf_exempt
def view_challenge(request):
    return render(request, 'sharepoint/challenge.html', {})

def get_completed_ideas():
    url = "/ideas"
    params = {
        "include": "creator,challenge",
        "include_descendants": False,
        "is_advisor_only": False,
        "order": "-created",
        "own_only": False,
        "page": 1,
        "page_size": 100,
        "status": "Completed",
    }
    response = make_request(url, params)
    return response['data']

# Create your views here.
@xframe_options_exempt
@csrf_exempt
def view_idea(request):
    ideas = get_completed_ideas()
    return render(
        request,
        'sharepoint/idea.html',
        {
            'ideas': ideas,
        },
    )

# Create your views here.
@xframe_options_exempt
@csrf_exempt
def add_idea(request):
    params = {
        'include_descendants': False,
        'order': '-created',
        'page': 1,
        'page_size': 10
    }
    challenges = make_request(
        url='/challenges',
        params=params,
    )
    challenges = challenges['data']
    return render(
        request,
        'sharepoint/challenge.html',
        {
            'challenges': challenges,
        },
    )