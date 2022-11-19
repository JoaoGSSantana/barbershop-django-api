web: gunicorn barbershop.wsgi:application --log-file --log-level debug
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver