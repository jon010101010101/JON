# Calculadora de BMI y clasificacion segun OMS

from give_bmi import give_bmi, apply_limit

def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Bajo peso"
    elif 18.5 <= bmi < 25:
        return "Peso normal"
    elif 25 <= bmi < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

if __name__ == "__main__":
    height_input = input("Ingresa la altura en metros (separado por punto): ")
    weight_input = input("Ingresa el peso en kilogramos: ")

    try:
        height_value = float(height_input)
        weight_value = float(weight_input)

        # Calcular el BMI
        bmi_value = give_bmi([height_value], [weight_value])[0]
        classification = classify_bmi(bmi_value)
        print(f"BMI: {bmi_value:.2f} - Clasificación: {classification}")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para la altura y el peso.")

    """
    
    Peso insufiente: IMC por debajo de 18,5
    Normopeso: IMC entre 18,5 y 24,9
    Sobrepeso: IMC entre 25 y 29,9
    Obesidad tipo I: IMC entre 30 y 34,9
    Obesidad tipo II: IMC entre 35 y 39,9
    Obesidad tipo III (mórbida): IMC entre 40 y 49,9
    Obesidad tipo IV (extrema): IMC mayor de 50

    
    """