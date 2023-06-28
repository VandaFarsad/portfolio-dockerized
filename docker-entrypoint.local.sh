#!/usr/bin/env bash

set -e

# install netcat for tcp-port-wait
apt-get update && apt-get install -y --no-install-recommends git

echo "Initializing..."
python manage.py wait_for_db

echo "Installing testing packages"
pip install -r requirements/development.txt

echo "Running migrations..."
python manage.py migrate

echo "Running Application. Visit admin page at http://localhost:8000/admin"
python manage.py runserver 0.0.0.0:8000
