
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
