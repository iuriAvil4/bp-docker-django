#!/bin/sh
echo "Esperando o PostgreSQL ficar pronto..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "PostgreSQL está pronto. Iniciando Django..."
python manage.py migrate
python manage.py runserver 0.0.0.0:8000