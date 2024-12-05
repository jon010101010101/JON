from datetime import datetime

# Obtiene la hora actual (marca de tiempo) en segundos desde el 1 de enero de 1970
marca_de_tiempo_actual = datetime.timestamp(datetime.now())

# Muestra la hora en segundos en notación decimal y científica
print(f"Segundos desde el 1 de enero de 1970: {marca_de_tiempo_actual:.4f} o {marca_de_tiempo_actual:.2e}")

# .: Especifica que queremos incluir decimales en el número.
# 4: Indica que queremos mostrar 4 lugares decimales.
# f: Especifica que queremos formatear el número como un número de punto flotante
# (decimal).

# :: Indica el comienzo de la especificación de formato.

# .2: Significa que queremos dos lugares decimales después del punto decimal.

# e: Indica que queremos formatear el número en notación científica o exponencial. En notación científica, los números se expresan como un coeficiente multiplicado por una potencia de diez, en la forma:
# a x 10 elevado a b

# Obtiene la fecha actual y la formatea como 'Mes Día Año'
fecha_formateada = datetime.now().strftime("%b %d %Y")
print(fecha_formateada)

# strftime significa "formato de cadena de tiempo."
# Convierte el objeto datetime en una cadena utilizando el formato especificado.

# %b: mes abreviado (por ejemplo, "Ene", "Feb", "Mar", etc.).
# %d: día del mes como un número decimal, con relleno de ceros si es necesario (por ejemplo, "01", "02", ..., "31").
# %Y: año como un número decimal de cuatro dígitos (por ejemplo, "2024").
# strftime: Una función de Python para formatear fechas. Proviene del módulo time
# o datetime.
