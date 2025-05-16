#!/bin/bash
# Script: listar_todo_proyectos.sh
# Lista superusuarios, usuarios normales y tips (con autor) de ex00 a ex06

for PROYECTO in ex00 ex01 ex02 ex03 ex04 ex05 ex06
do
    echo "============================"
    echo "     Proyecto: $PROYECTO"
    echo "============================"
    cd ../$PROYECTO || { echo "No se pudo entrar a $PROYECTO"; continue; }

    if [[ "$PROYECTO" == "ex06" ]]; then
python manage.py shell << EOF
from tips.models import CustomUser, Tip

print("=== SUPERUSUARIOS ===")
for user in CustomUser.objects.filter(is_superuser=True):
    print(f"- {user.username} ({user.email})")

print("\n=== USUARIOS NORMALES ===")
for user in CustomUser.objects.filter(is_superuser=False):
    print(f"- {user.username} ({user.email})")

print("\n=== TIPS ===")
for tip in Tip.objects.all():
    print(f"- {tip.title} (autor: {tip.author.username})")
EOF

    elif [[ "$PROYECTO" =~ ^ex0[2-5]$ ]]; then
python manage.py shell << EOF
from django.contrib.auth.models import User
from lifetips.tips.models import Tip

print("=== SUPERUSUARIOS ===")
for user in User.objects.filter(is_superuser=True):
    print(f"- {user.username} ({user.email})")

print("\n=== USUARIOS NORMALES ===")
for user in User.objects.filter(is_superuser=False):
    print(f"- {user.username} ({user.email})")

print("\n=== TIPS ===")
for tip in Tip.objects.all():
    print(f"- {tip.content[:30]} (autor: {tip.author.username})")
EOF

    else
python manage.py shell << EOF
from django.contrib.auth.models import User

print("=== SUPERUSUARIOS ===")
for user in User.objects.filter(is_superuser=True):
    print(f"- {user.username} ({user.email})")

print("\n=== USUARIOS NORMALES ===")
for user in User.objects.filter(is_superuser=False):
    print(f"- {user.username} ({user.email})")
EOF
    fi

    cd - > /dev/null
    echo
done



#./listar_todo.sh