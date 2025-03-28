import sys
import os
from path import Path

# Add local_lib to PYTHONPATH. para que encuentre la ruta desde cualquier sitio
sys.path.append(os.path.abspath("local_lib"))

def main():
    # Crear una carpeta
    folder = Path("my_folder")
    folder.mkdir_p()

    # Crear un archivo dentro de la carpeta
    file = folder / "my_file.txt"
    
    # Escribir en el archivo
    file.write_text("¡Hola desde path.py!")

    # Leer y mostrar el contenido del archivo
    content = file.read_text()
    print(f"Contenido del archivo: {content}")

if __name__ == '__main__':
    main()

