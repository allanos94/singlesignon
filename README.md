# Wazoku Integrations test

## Description
This repo is intended for testing Single Sign On with Google accounts and interactions with its API.

## Getting started

Copying the repository

Due to the public nature of forks we suggest you duplicate the repo rather then forking it.
You will need to create your own repo e.g. `[your_github_username]/singlesignon` and then clone
this repo `eshwaric/singlesignon` and push the code into your new one. You can follow the steps for doing this here: https://help.github.com/articles/duplicating-a-repository/

Before proceeded be aware that this exercise assumes you are using a linux machine with [pip](https://pip.pypa.io/en/stable) and [venv](https://docs.python.org/3/library/venv.html) installed.

Create a new virtualenv in your checked out repo.

    cd /[path_to]/singlesignon
    python3 -m venv ve


Then install the dependencies:

    ./ve/bin/pip install -r requirements.txt


Set the default django settings file used by all following commands:

    export DJANGO_SETTINGS_MODULE=integrationsite.settings


The code in this repo uses an sqlite database as the persistence layer. You can initialize an sqlite database (this db will be stored in the file `./db.sqlite3`)

    bin/python manage.py migrate

The web application has an INSTALLED_APP called which handles single sign on using Google accounts. The app has a model called User which stores user info.


## Exercise
index.html is a very simple webpage which just has a Login with Google button. Implement single sign on with Google using the OAuth Protocol and create a user for the web application. The profile details of the user must be pulled from google and persisted in the app.

Please create a pull request for this work. Bonus marks for adding tests for the integration


