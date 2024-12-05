
    Primera llamada:

python
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")

a) La función recibe los valores 1, 42, 360, 11, 64 como argumentos posicionales 
(*args) y tres argumentos con nombre (**kwargs): toto="mean", tutu="median", 
tata="quartile". 
b) Se crea una lista ordenada de los valores: [1, 11, 42, 64, 360]
c) Para cada operación en kwargs:

    "mean":
        Suma de valores: 1 + 42 + 360 + 11 + 64 = 478
        Número de valores: 5
        Media: 478 / 5 = 95.6
        Imprime: "mean : 95.6"
    "median":
        Con 5 valores (impar), se toma el valor central de la lista ordenada
        Mediana: 42
        Imprime: "median : 42.0"
    "quartile": se ordenan y redondean para series pequeñas
        Para Q1 (25%): índice = 5 // 4 = 1, valor = 11
        Para Q3 (75%): índice = 5 * 3 // 4 = 3, valor = 64
        Imprime: "quartile : [11.0, 64.0]"

print("-----")

    Segunda llamada:

python
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")

a) Valores: [5, 75, 450, 18, 597, 27474, 48575]
b) Operaciones: "std" y "var"
c) Para cada operación:

    "var" (varianza):
        Calcula la media: (5 + 75 + 450 + 18 + 597 + 27474 + 48575) / 7 = 11027.714285714286
        Suma de cuadrados de diferencias: ((5-11027.714285714286)^2 + ... + (48575-11027.714285714286)^2) / 7
        Varianza: 308708251.26530612
        Imprime: "var : 308708251.26530612"
    "std" (desviación estándar):
        Raíz cuadrada de la varianza: √308708251.26530612 = 17569.94066340057
        Imprime: "std : 17569.94066340057"

print("-----")

    Tercera llamada:

python
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")

a) Valores: [5, 75, 450, 18, 597, 27474, 48575]
b) Operaciones: "heheh" y "kdekem"
c) Como estas operaciones no están definidas en la función, no se realiza ningún cálculo
 ni se imprime nada. print("-----")

print("-----")

    Cuarta llamada:

python
ft_statistics(toto="mean", tutu="median", tata="quartile")

a) No se proporcionan valores numéricos (*args está vacío)
b) Operaciones: "mean", "median", "quartile"
c) Para cada operación:

    Se lanza una excepción AssertionError porque no hay valores para calcular
    Se imprime: "ERROR" para cada operación

Este es el proceso paso a paso de cómo la función ft_statistics maneja cada llamada
 y produce los resultados correspondientes.