#!/bin/bash

# Display pip version
echo "Pip version:"
pip --version

# Install path.py development version from GitHub into local_lib
echo "Installing path.py..."
pip install --upgrade git+https://github.com/jaraco/path.py.git -t ./local_lib > path_install.log 2>&1

# Verify installation
if [ $? -eq 0 ]; then
    echo "path.py installed successfully. Logs saved in path_install.log"
    # Execute the Python program with PYTHONPATH
    PYTHONPATH=./local_lib python my_program.py
else
    echo "Error installing path.py. Check path_install.log for details."
fi




# ./my_script.sh
# cat my_folder/my_file.txt

