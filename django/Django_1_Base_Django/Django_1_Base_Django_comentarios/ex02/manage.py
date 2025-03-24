#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os
import sys


def main():
    """Ejecuta tareas administrativas."""
    # Configura la variable de entorno para el módulo de configuración de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Intenta importar la función para ejecutar comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, lanza un error con un mensaje explicativo
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando de Django pasado como argumento
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Si este script se ejecuta directamente, llama a la función main()
    main()



# python manage.py makemigrations
# python manage.py migrate

# python manage.py runserver
# http://localhost:8000/ex02/




# pkill -f "python manage.py runserver"
# lsof -i :8000
# kill -9 38140