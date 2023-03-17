#!/bin/bash

# This is the entrypoint used by the docker container

# The migrations for the mock app are completely auto-generated from its models.
# They don't live in git.
python manage.py makemigrations app

python manage.py migrate

echo "Creating superuser with admin:admin login"
echo "from django.contrib.auth.models import User;User.objects.create_superuser('admin', 'admin@example.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

python manage.py runserver 0.0.0.0:8000
