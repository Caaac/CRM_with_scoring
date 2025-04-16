#!/bin/sh
while ! nc -z db 3306; do
  echo "Waiting for MySQL..."
  sleep 1
done

sleep 5;
python manage.py runserver 0.0.0.0:8000