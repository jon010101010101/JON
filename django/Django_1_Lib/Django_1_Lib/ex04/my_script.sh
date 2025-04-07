#!/bin/bash

# Deactivate the current virtual environment if it is active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    deactivate
    echo "🔄 Previous virtual environment '$VIRTUAL_ENV' deactivated."
fi

# Create a virtual environment in Python 3 called django_venv
python3 -m venv django_venv  

# Activate the virtual environment
source django_venv/bin/activate

# Install the requirements from the requirements.txt file
pip install -r requirement.txt  # Note: Make sure to change 'requirement.txt' to 'requirements.txt'

echo "✅ Environment 'django_venv' configured and activated."


# pip install -r requirement.txt
# chmod +x my_script.sh
# source ./my_script.sh


