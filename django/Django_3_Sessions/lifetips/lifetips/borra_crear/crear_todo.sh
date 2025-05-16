#!/bin/bash
# Script: limpiar_y_crear_todo_global.sh
# Limpia todo y crea usuarios y tips globales según el enunciado

for PROYECTO in ex00 ex01 ex02 ex03 ex04 ex05 ex06
do
    echo "============================"
    echo "   Limpiando y creando en $PROYECTO"
    echo "============================"
    cd ../$PROYECTO || { echo "No se pudo entrar a $PROYECTO"; continue; }

    if [[ "$PROYECTO" == "ex06" ]]; then
python manage.py shell << EOF
from tips.models import CustomUser, Tip

# Limpieza
Tip.objects.all().delete()
CustomUser.objects.all().delete()

# Crear superusuario global
if not CustomUser.objects.filter(username='admin_global').exists():
    CustomUser.objects.create_superuser(username='admin_global', password='adminpass', email='admin_global@correo.com')
    print("ex06: superusuario admin_global creado")
else:
    print("ex06: superusuario admin_global ya existe")

# Crear 5 usuarios normales y 3 tips por usuario
for i in range(1, 6):
    uname = f"user_{i:02d}"
    if not CustomUser.objects.filter(username=uname).exists():
        user = CustomUser.objects.create_user(username=uname, password='userpass', email=f"{uname}@correo.com")
        print(f"ex06: usuario normal {uname} creado")
    else:
        user = CustomUser.objects.get(username=uname)
        print(f"ex06: usuario normal {uname} ya existe")
    # Crear 3 tips para cada usuario
    for t in range(1, 4):
        if not Tip.objects.filter(author=user, title=f"Tip {t} de {uname}").exists():
            Tip.objects.create(title=f"Tip {t} de {uname}", content=f"Este es el tip {t} de {uname}", author=user)
            print(f"ex06: tip {t} para {uname} creado")
        else:
            print(f"ex06: tip {t} para {uname} ya existe")
EOF

    elif [[ "$PROYECTO" =~ ^ex0[2-5]$ ]]; then
python manage.py shell << EOF
from django.contrib.auth.models import User
from lifetips.tips.models import Tip

# Limpieza
Tip.objects.all().delete()
User.objects.all().delete()

# Crear superusuario global
if not User.objects.filter(username='admin_global').exists():
    User.objects.create_superuser(username='admin', password='adminpass', email='admin_global@correo.com')
    print("$PROYECTO: superusuario admin_global creado")
else:
    print("$PROYECTO: superusuario admin_global ya existe")

# Crear 2 usuarios normales y 2 tips por usuario
for i in range(1, 3):
    uname = f"user_{i:02d}"
    if not User.objects.filter(username=uname).exists():
        user = User.objects.create_user(username=uname, password='userpass', email=f"{uname}@correo.com")
        print(f"$PROYECTO: usuario normal {uname} creado")
    else:
        user = User.objects.get(username=uname)
        print(f"$PROYECTO: usuario normal {uname} ya existe")
    # Crear 2 tips para cada usuario
    for t in range(1, 3):
        if not Tip.objects.filter(author=user, content=f"Este es el tip {t} de {uname}").exists():
            Tip.objects.create(content=f"Este es el tip {t} de {uname}", author=user)
            print(f"$PROYECTO: tip {t} para {uname} creado")
        else:
            print(f"$PROYECTO: tip {t} para {uname} ya existe")
EOF

    else
python manage.py shell << EOF
from django.contrib.auth.models import User

# Limpieza
User.objects.all().delete()

# Crear superusuario global
if not User.objects.filter(username='admin_global').exists():
    User.objects.create_superuser(username='admin_global', password='adminpass', email='admin_global@correo.com')
    print("$PROYECTO: superusuario admin_global creado")
else:
    print("$PROYECTO: superusuario admin_global ya existe")

# Crear 2 usuarios normales
for i in range(1, 3):
    uname = f"user_{i:02d}"
    if not User.objects.filter(username=uname).exists():
        User.objects.create_user(username=uname, password='userpass', email=f"{uname}@correo.com")
        print(f"$PROYECTO: usuario normal {uname} creado")
    else:
        print(f"$PROYECTO: usuario normal {uname} ya existe")
EOF
    fi

    cd - > /dev/null
    echo
done
