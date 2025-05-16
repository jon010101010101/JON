#!/bin/bash
# Script: limpiar_todo.sh
# Borra todos los superusuarios, usuarios normales y tips en ex00 a ex06

for PROYECTO in ex00 ex01 ex02 ex03 ex04 ex05 ex06
do
    echo "============================"
    echo "   Limpiando $PROYECTO"
    echo "============================"
    cd ../$PROYECTO || { echo "No se pudo entrar a $PROYECTO"; continue; }

    if [[ "$PROYECTO" == "ex06" ]]; then
python manage.py shell << EOF
from tips.models import Tip, CustomUser

Tip.objects.all().delete()
CustomUser.objects.all().delete()
print("ex06: Todos los usuarios y tips borrados.")
EOF

    elif [[ "$PROYECTO" =~ ^ex0[2-5]$ ]]; then
python manage.py shell << EOF
from lifetips.tips.models import Tip
from django.contrib.auth.models import User

Tip.objects.all().delete()
User.objects.all().delete()
print("$PROYECTO: Todos los usuarios y tips borrados.")
EOF

    else
python manage.py shell << EOF
from django.contrib.auth.models import User

User.objects.all().delete()
print("$PROYECTO: Todos los usuarios borrados (no hay tips en este proyecto).")
EOF
    fi

    cd - > /dev/null
    echo
done



# ./limpiar_tips_y_usuarios.sh