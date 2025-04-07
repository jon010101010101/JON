#!/bin/bash # es el interprete que va a usar de bash, sin esta linea podri adar errores

# Desactivar el entorno virtual actual si está activo
if [[ "$VIRTUAL_ENV" != "" ]]; then
    deactivate
    echo "🔄 Entorno virtual anterior '$VIRTUAL_ENV' desactivado."
fi

# Crear un entorno virtual en python3 llamado django_venv
python3 -m venv django_venv  

# Activar el entorno virtual
source django_venv/bin/activate

# Instalar los requisitos del archivo requirements.txt
pip install -r requirement.txt 

echo "✅ Entorno 'django_venv' configurado y activado."




# chmod +x my_script.sh
# source ./my_script.sh

