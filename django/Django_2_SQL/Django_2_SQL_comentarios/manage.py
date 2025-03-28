#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exx00.d00_proyect.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()




# docker-compose up --build
# docker-compose ps


# docker-compose exec web python manage.py makemigrations
# docker-compose exec web python manage.py migrate
# docker-compose exec web python manage.py runserver 0.0.0.0:8080

# http://127.0.0.1:8080


# pkill -f "python manage.py runserver"
# lsof -i :8080
# kill -9 38145