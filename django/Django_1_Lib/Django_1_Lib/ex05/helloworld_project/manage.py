#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """
    Run administrative tasks.

    This function sets up the Django environment, imports the necessary functions,
    and executes the provided administrative commands.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld_project.settings')
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





# en helloworld_project
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 8080
# http://localhost:8080

# pkill -f "python manage.py runserver"
# lsof -i :8080
# kill -9 38145