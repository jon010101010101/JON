#!/bin/sh
# wait_for_db.sh

# Espera hasta que el servicio de base de datos esté disponible
echo "Esperando a que PostgreSQL esté disponible..."
while ! nc -z db 5432 || ! pg_isready -h db -U djangouser -d d42; do
  echo "PostgreSQL no está listo aún. Intentando nuevamente..."
  sleep 2
done

echo "PostgreSQL está disponible. Iniciando Django."
exec "$@"  # Ejecuta el comando pasado como argumento (por ejemplo, iniciar Django)
