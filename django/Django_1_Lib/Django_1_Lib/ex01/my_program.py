import sys
import os
from path import Path

# Add local_lib to PYTHONPATH
sys.path.append(os.path.abspath("local_lib"))

def main():
    # Create a folder
    folder = Path("my_folder")
    folder.mkdir_p()

    # Create a file inside the folder
    file = folder / "my_file.txt"
    
    # Write to the file
    file.write_text("Hello from path.py!")

    # Read and display the file contents
    content = file.read_text()
    print(f"File contents: {content}")

if __name__ == '__main__':
    main()

