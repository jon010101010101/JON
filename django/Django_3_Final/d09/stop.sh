#!/bin/bash

echo "Parando Redis..."
pkill -f redis-server && echo "Redis parado." || echo "Redis no estaba en marcha."

echo "Buscando procesos Django runserver..."
RUNSERVER_PIDS=$(ps aux | grep "manage.py runserver" | grep -v grep | awk '{print $2}')
if [ -z "$RUNSERVER_PIDS" ]; then
    echo "No hay procesos Django runserver en marcha."
else
    echo "Matando procesos Django runserver con PID(s): $RUNSERVER_PIDS"
    kill -9 $RUNSERVER_PIDS
    echo "Django runserver parado."
fi

echo "Buscando procesos Daphne..."
DAPHNE_PIDS=$(ps aux | grep daphne | grep -v grep | awk '{print $2}')
if [ -z "$DAPHNE_PIDS" ]; then
    echo "No hay procesos Daphne en marcha."
else
    echo "Matando procesos Daphne con PID(s): $DAPHNE_PIDS"
    kill -9 $DAPHNE_PIDS
    echo "Daphne parado."
fi


# ./stop.sh