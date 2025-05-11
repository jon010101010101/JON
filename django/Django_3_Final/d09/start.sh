#!/bin/bash

# 1. Arranca Redis en segundo plano si no está ya corriendo
if ! pgrep -f redis-server > /dev/null; then
    /sgoinfre/students/jurrutia/redis-stable/src/redis-server &
    echo "Redis arrancado."
else
    echo "Redis ya está corriendo."
fi

# 2. Activa el entorno conda llamado "Final"
source /sgoinfre/students/jurrutia/sgoinfre/miniforge3/etc/profile.d/conda.sh
conda activate Final
echo "Entorno conda 'Final' activado."

# 3. Arranca Django
python manage.py runserver



# ./start.sh
