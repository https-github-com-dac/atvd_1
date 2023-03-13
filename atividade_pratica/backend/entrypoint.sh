#!/bin/bash

python3 -m venv env

env/bin/pip install -r requirements.txt

env/bin/python3 manage.py makemigrations
env/bin/python3 manage.py migrate

env/bin/python3 manage.py createsuperuser --username admin --email admin@admin.com
