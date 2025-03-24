# Importa la función render de django.shortcuts para renderizar plantillas HTML
from django.shortcuts import render

# Define la vista color_table
def color_table(request):
    # Lista de colores que se mostrarán en la tabla
    colors = ['noir', 'rouge', 'bleu', 'vert']
    rows = []
    
    # Genera 50 filas de tonalidades de colores
    for i in range(50):
        row = []
        for color in colors:
            # Genera un tono de color diferente para cada color
            if color == 'noir':
                # Negro: todas las componentes RGB son iguales
                shade = f'#{i*5:02x}{i*5:02x}{i*5:02x}'
            elif color == 'rouge':
                # Rojo: solo la componente R varía
                shade = f'#{i*5:02x}0000'
            elif color == 'bleu':
                # Azul: solo la componente B varía
                shade = f'#0000{i*5:02x}'
            else:  # vert
                # Verde: solo la componente G varía
                shade = f'#00{i*5:02x}00'
            row.append(shade)
        rows.append(row)

    # Prepara el contexto para la plantilla
    context = {
        'colors': colors,
        'rows': rows,
    }
    
    # Renderiza la plantilla 'table_app/color_table.html' con el contexto
    return render(request, 'table_app/color_table.html', context)
