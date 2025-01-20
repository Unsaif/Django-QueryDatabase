#!/bin/bash

# Wait until the MySQL service is ready
echo "Waiting for the MySQL database to be ready..."
while ! nc -z db 3306; do
  sleep 1
done

echo "MySQL is ready! Starting Django server..."
python3 manage.py runserver 0.0.0.0:8001