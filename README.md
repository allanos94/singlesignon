# Demo Polls Application

## Description
This repo is intended for testing a simple polls application which captures answers to poll questions from users. Polls are linked to client and each client can have their own user profile form. The application uses Django's in-built Authentication system (https://docs.djangoproject.com/en/3.2/topics/auth/).

## Getting started

Copying the repository

Due to the public nature of forks we suggest you duplicate the repo rather then forking it.
You will need to create your own repo e.g. `[your_github_username]/singlesignon` and then clone
this repo `eshwaric/singlesignon` and push the code into your new one. You can follow the steps for doing this here: https://help.github.com/articles/duplicating-a-repository/

Before proceeding be aware that this exercise assumes you are using a linux machine with [pip](https://pip.pypa.io/en/stable) and [venv](https://docs.python.org/3/library/venv.html) installed.

To initialize the repository run the below script
./initialize_repo.sh

This script will install Django 3.2 and other libraries required for the application. It also loads a fixture to prepopulate the database with some test data for the application

To start the webserver locally, execute the below command in your base directory
./run-server.sh

To run tests locally, execute the below command in your base directory
./run-tests.sh

