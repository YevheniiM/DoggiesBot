release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 2 --threads 8 dtb.wsgi:application
worker: celery -A dtb worker -P solo --loglevel=INFO
beat: celery -A dtb beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
