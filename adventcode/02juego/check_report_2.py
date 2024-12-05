def is_safe(report):
    """Determina si un informe es seguro."""
    # Verificar si el informe es estrictamente creciente o decreciente
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(-3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe_with_one_removal(report):
    """Verifica si un informe puede ser seguro al eliminar un solo nivel."""
    for i in range(len(report)):
        # Crear una copia del informe sin el i-ésimo nivel
        modified_report = report[:i] + report[i+1:]
        # Verificar si el informe modificado es seguro
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(file_path):
    """Cuenta cuántos informes son seguros a partir de un archivo, considerando el problema Dampener."""
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            # Comprobar si el informe es seguro o si puede serlo eliminando un solo nivel
            if is_safe(report) or can_be_safe_with_one_removal(report):
                safe_count += 1
    return safe_count

# Ruta del archivo de entrada
file_path = "input02juego2"

# Calcular y mostrar el resultado
safe_reports = count_safe_reports(file_path)
print(f"Cantidad de informes seguros: {safe_reports}")

