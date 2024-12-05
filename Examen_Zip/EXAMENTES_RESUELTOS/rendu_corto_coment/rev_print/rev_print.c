/*
Assignment name  : rev_print
Expected files   : rev_print.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string, and displays the string in reverse
followed by a newline.
If the number of parameters is not 1, the program displays a newline.
-------------------------------------------------- ------------------------------
Escribe un programa que tome una cadena y la muestre al revés
seguido de una nueva línea.
Si el número de parámetros no es 1, el programa muestra una nueva línea.

Examples:
$> ./rev_print "zaz" | cat -e
zaz$
$> ./rev_print "dub0 a POIL" | cat -e
LIOP a 0bud$
$> ./rev_print | cat -e
$
*/

#include <unistd.h>  // Incluye la biblioteca estándar para usar la función write

int main(int argc, char **argv)
{
    // Verifica si se ha proporcionado exactamente un argumento adicional
    if (argc == 2)
    {
        int i = 0;

        // Primer bucle 'while' para calcular la longitud de la cadena
        while (argv[1][i])
            i++;
        
        // Segundo bucle 'while' para imprimir la cadena al revés
        while (i > 0)
        {
            // Escribe el carácter en la posición 'i-1' de 'argv[1]'. i-1 para imprimir al revés.
            write(1, &argv[1][i-1], 1); 
            i--;
        }
    }

    // Imprime una nueva línea al final para asegurar que la salida sea legible
    write(1, "\n", 1);
    return (0);  // Termina el programa exitosamente
}

