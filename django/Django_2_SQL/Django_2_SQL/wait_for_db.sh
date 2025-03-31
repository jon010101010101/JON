#!/bin/bash
# wait_for_db.sh

# Espera hasta que el servicio de base de datos esté disponible
while ! nc -z db 5432; do
  echo "Esperando a que PostgreSQL esté disponible..."
  sleep 2  # Aumenta el tiempo de espera
done

echo "PostgreSQL está disponible. Iniciando Django."
exec "$@"