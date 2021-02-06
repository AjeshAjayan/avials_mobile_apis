#!/bin/sh

#python manage.py wait_for_db
#python manage.py migrate
#python manage.py load_initial_data
gunicorn --env DJANGO_SETTINGS_MODULE=avials_mobile_apis.settings.dev --bind 0.0.0.0:8000 avials_mobile_apis.wsgi:application --timeout 300
