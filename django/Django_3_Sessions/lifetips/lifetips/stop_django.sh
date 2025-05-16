#!/bin/bash

echo "Buscando procesos Django runserver..."
RUNSERVER_PIDS=$(ps aux | grep "manage.py runserver" | grep -v grep | awk '{print $2}')

if [ -z "$RUNSERVER_PIDS" ]; then
    echo "No hay procesos Django runserver en marcha."
else
    echo "Matando procesos Django runserver con PID(s): $RUNSERVER_PIDS"
    kill -9 $RUNSERVER_PIDS
    echo "Django runserver parado."
fi


# ./stop_django.sh