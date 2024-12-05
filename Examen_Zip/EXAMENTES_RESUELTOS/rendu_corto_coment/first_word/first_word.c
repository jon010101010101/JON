/* Assignment name  : first_word
Expected files   : first_word.c
Allowed functions: write
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y muestre su primera palabra, seguida 
de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o 
por el inicio/final de la cuerda.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

Write a program that takes a string and displays its first word, followed by a
newline.A word is a section of string delimited by spaces/tabs or by the start/end of
the string.
If the number of parameters is not 1, or if there are no words, simply displaya newline.
Examples:
$> ./first_word "FOR PONY" | cat -e
FOR$
$> ./first_word "this        ...       is sparta, then again, maybe    not" | cat -e
this$
$> ./first_word "   " | cat -e
$
$> ./first_word "a" "b" | cat -e
$
$> ./first_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$> */

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h> // Incluye la biblioteca para usar la función write

#define SU argv[1][i] // Define un alias 'SU' para simplificar el acceso al carácter actual de la cadena de argumentos

int main(int argc, char **argv)
{
    // Verifica si se ha proporcionado exactamente un argumento adicional
    if (argc == 2)
    {
        int i = 0; // Inicializa el índice para recorrer la cadena de caracteres del argumento

        // Avanza en la cadena saltando cualquier espacio en blanco inicial (' ' o '\t')
        while (SU == 32 || SU == 9) // 32 es el código ASCII de ' ' y 9 es el de '\t'
            i++;

        // Imprime los caracteres de la palabra que se encuentra a continuación de los espacios en blanco
        // Continuará mientras SU sea un carácter imprimible entre el rango 33 y 126 en ASCII
        while (SU >= 33 && SU <= 126)
        {
            write(1, &SU, 1); // Imprime el carácter actual
            i++; // Incrementa el índice para avanzar al siguiente carácter
        }
    }
    write(1, "\n", 1); // Imprime un salto de línea al final para asegurar que la salida sea legible
    return (0); // Retorna 0 para indicar que el programa ha finalizado correctamente
}

