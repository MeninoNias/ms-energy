#!/bin/sh

python manage.py migrate
python manage.py create_superuser_if_not_exists
gunicorn --bind 0.0.0.0:8000 energy.wsgi:application