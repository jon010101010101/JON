#!/bin/bash

# Arranca Redis (si no está ya corriendo)
if ! pgrep -x "redis-server" > /dev/null
then
    echo "Iniciando Redis..."
    redis-server &
    sleep 2
else
    echo "Redis ya está corriendo."
fi

# Arranca Daphne (en el puerto 8000, cambia si necesitas otro)
echo "Iniciando Daphne..."
daphne -b 0.0.0.0 -p 8000 d09.asgi:application


# ./start.sh
