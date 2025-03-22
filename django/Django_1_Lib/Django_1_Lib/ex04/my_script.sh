#!/bin/bash

# Create a Python3 virtual environment named django_venv
python3 -m virtualenv django_venv

# Activate the virtual environment
source django_venv/bin/activate

# Install the requirements from the requirement.txt file
pip install -r requirement.txt

# Final message
echo "✅ Environment configured. Run to activate:"
echo "source django_venv/bin/activate"




# pip install -r requirement.txt
# chmod +x my_script.sh
# ./my_script.sh

