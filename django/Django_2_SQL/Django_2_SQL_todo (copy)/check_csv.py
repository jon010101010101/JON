import csv
import os

def check_csv(file_name):
    # Ruta al archivo CSV
    csv_path = os.path.join('ex08', 'data', file_name)

    try:
        # Leer el archivo y mostrar las filas
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            print(f"Contenido de {file_name}:")
            for row in reader:
                print(row)  # Imprime cada fila para verificar su formato
    except Exception as e:
        print(f"Error leyendo {file_name}: {e}")

if __name__ == "__main__":
    # Verificar ambos archivos CSV
    check_csv('people.csv')
    check_csv('planets.csv')
