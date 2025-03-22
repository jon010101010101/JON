# Ensure using Python from the conda environment
export PATH="/home/jurrutia/miniforge3/envs/django_env/bin:$PATH"

# Display pip version
echo "Pip version:"
python -m pip --version

# Update pip
echo "Updating pip..."
python -m pip install --upgrade pip # Updates pip to the latest available version.

# Install path.py globally in the environment
echo "Installing path.py..." 
python -m pip install path.py  # Installs the path.py package

# Verify if the installation was successful
if [ $? -eq 0 ]; then
    echo "path.py installed successfully."
    # Execute the Python program
    python my_program.py
else
    echo "Error installing path.py."
fi



# ./my_script.sh
# cat my_folder/my_file.txt

