#!/usr/bin/env python
"""Utilidad de línea de comandos de Django para tareas administrativas."""
import os
import sys


def main():
    """Ejecutar tareas administrativas."""
    # Configura el módulo de configuración de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd05.settings')
    try:
        # Intenta importar la función para ejecutar comandos de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si no se puede importar Django, lanza un error informativo
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
