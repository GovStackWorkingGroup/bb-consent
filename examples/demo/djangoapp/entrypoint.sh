#!/bin/bash

# This is the entrypoint used by the docker container

python manage.py runserver 0.0.0.0:8000
