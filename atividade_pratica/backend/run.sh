#!/bin/bash

env/bin/python3 manage.py makemigrations
env/bin/python3 manage.py migrate

env/bin/python3 manage.py runserver
