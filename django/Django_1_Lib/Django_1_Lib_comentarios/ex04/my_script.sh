#!/bin/bash # es el interprete que va a usar de bash, sin esta linea podri adar errores

# Crear virtualenv en python3 llamado django_venv
python3 -m virtualenv django_venv

# Activar el virtualenv
source django_venv/bin/activate

# Instalar los requisitos del archivo requirement.txt
pip install -r requirement.txt

echo "✅ Entorno configurado y activado."




# chmod +x my_script.sh
# source ./my_script.sh

