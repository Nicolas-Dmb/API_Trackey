release: python /app/trackey/manage.py collectstatic --noinput
web: gunicorn trackey.wsgi --log-file -
