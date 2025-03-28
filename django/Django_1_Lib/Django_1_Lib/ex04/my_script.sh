#!/bin/bash

# Create a Python3 virtual environment named django_venv
python3 -m virtualenv django_venv

# Install the requirements from the requirement.txt file
django_venv/bin/pip install -r requirement.txt

# Activate the virtual environment
source django_venv/bin/activate

# Final message
echo "✅ Environment configured and activated."





# pip install -r requirement.txt
# chmod +x my_script.sh
# source ./my_script.sh


