from django.shortcuts import render

def color_table(request):
    colors = ['noir', 'rouge', 'bleu', 'vert']
    rows = []
    for i in range(50):
        row = []
        for color in colors:
            if color == 'noir':
                shade = f'#{i*5:02x}{i*5:02x}{i*5:02x}'
            elif color == 'rouge':
                shade = f'#{i*5:02x}0000'
            elif color == 'bleu':
                shade = f'#0000{i*5:02x}'
            else:  # vert
                shade = f'#00{i*5:02x}00'
            row.append(shade)
        rows.append(row)

    context = {
        'colors': colors,
        'rows': rows,
    }
    return render(request, 'table_app/color_table.html', context)
