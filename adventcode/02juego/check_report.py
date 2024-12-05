def is_safe(report):
    """Determina si un informe es seguro."""
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(-3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(file_path):
    """Cuenta cuántos informes son seguros a partir de un archivo."""
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count += 1
    return safe_count

# Ruta del archivo de entrada
file_path = "input02juego"

# Calcular y mostrar el resultado
safe_reports = count_safe_reports(file_path)
print(f"Cantidad de informes seguros: {safe_reports}")
