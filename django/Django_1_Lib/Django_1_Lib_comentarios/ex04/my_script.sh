#!/bin/bash # es el interprete que va a usar de bash, sin esta linea podri adar errores

# Crear virtualenv en python3 llamado django_venv
python3 -m virtualenv django_venv

# Activar el virtualenv
source django_venv/bin/activate

# Instalar los requisitos del archivo requirement.txt
pip install -r requirement.txt

# Mensaje final
echo "✅ Entorno configurado. Ejecuta para activar:"
echo "source django_venv/bin/activate"




# chmod +x my_script.sh
# ./my_script.sh

