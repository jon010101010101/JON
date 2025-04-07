#!/bin/bash

# Show the version of pip
echo "Pip version:"
python -m pip --version

# Define the local_lib directory
LIB_DIR="./local_lib"

# Remove the local_lib directory if it exists
if [ -d "$LIB_DIR" ]; then
    echo "Removing existing local_lib directory..."
    rm -rf "$LIB_DIR"
fi

# Create the local_lib directory
mkdir -p "$LIB_DIR"

# Install the development version of path.py from GitHub into local_lib
echo "Installing path.py..."
pip install --upgrade git+https://github.com/jaraco/path.py.git -t "$LIB_DIR" > path_install.log 2>&1

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "path.py installed successfully."
    # Execute the Python program with PYTHONPATH
    PYTHONPATH="$LIB_DIR" python my_program.py
else
    echo "Error installing path.py. Check path_install.log for more details."
fi


# ./my_script.sh
# cat my_folder/my_file.txt

