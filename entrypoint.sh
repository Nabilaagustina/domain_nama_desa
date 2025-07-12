#!/bin/sh

echo "Waiting for mysql..."
while ! nc -z db 3306; do
  sleep 1
done
echo "MySQL started"

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn --bind 0.0.0.0:8000 domain_nama_desa.wsgi:application
