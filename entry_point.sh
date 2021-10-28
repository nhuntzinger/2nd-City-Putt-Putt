#!/bin/bash

python manage.py makemigrations
until python manage.py migrate; do
    sleep 2
    echo "Retry!";
done

python manage.py makemigrations
python manage.py migrate

echo "Django is ready.";

python manage.py runserver 0.0.0.0:8000
