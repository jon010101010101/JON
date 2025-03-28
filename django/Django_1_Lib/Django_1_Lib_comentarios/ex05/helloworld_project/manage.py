#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os  # Importa el módulo os para interactuar con el sistema operativo
import sys  # Importa el módulo sys para acceder a variables y funciones específicas del sistema

def main():
    """
    Ejecuta tareas administrativas.

    Esta función configura el entorno de Django, importa las funciones necesarias
    y ejecuta los comandos administrativos proporcionados.
    """
    # Establece el módulo de configuración de Django por defecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld_project.settings')
    try:
        # Intenta importar la función execute_from_command_line de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, lanza una excepción con un mensaje informativo
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar un entorno virtual?"
        ) from exc
    # Ejecuta el comando de línea proporcionado
    execute_from_command_line(sys.argv)

# Verifica si este script se está ejecutando como programa principal
if __name__ == '__main__':
    main()  # Llama a la función principal



# en helloworld_project
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 8080
# http://localhost:8080

# pkill -f "python manage.py runserver"
# lsof -i :8080
# kill -9 38145