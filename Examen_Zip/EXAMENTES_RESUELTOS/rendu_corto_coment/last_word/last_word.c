/*Assignment name  : last_word
Expected files   : last_word.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays its last word followed by a \n.
A word is a section of string delimited by spaces/tabs or by the start/end of
the string.
If the number of parameters is not 1, or there are no words, display a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y muestre su última palabra seguida 
de \n.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o 
por el inicio/final de la cadena.
Si el número de parámetros no es 1 o no hay palabras, muestre una nueva línea.

Example:
$> ./last_word "FOR PONY" | cat -e
PONY$
$> ./last_word "this        ...       is sparta, then again, maybe    not" | cat -e
not$
$> ./last_word "   " | cat -e
$
$> ./last_word "a" "b" | cat -e
$
$> ./last_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>*/

#include <unistd.h>  // Incluye la biblioteca estándar para usar la función write

#define SU_MENOS argv[1][i - 1]  // Define un alias 'SU_MENOS' para acceder al carácter anterior en el primer argumento

int main(int argc, char **argv)
{
    int i = 0;          // Índice para recorrer la cadena
    int end = 0;        // Índice que marca el final de la última palabra encontrada
    int start = 0;      // Índice que marca el inicio de la última palabra encontrada

    // Verifica si se ha proporcionado exactamente un argumento adicional
    if (argc == 2)
    {
        // Encuentra la longitud total de la cadena del primer argumento
        while (argv[1][i])
            i++;
        
        // Mueve el índice hacia atrás ignorando espacios y tabulaciones al final de la cadena
        while (i > 0 && (SU_MENOS == 32 || SU_MENOS == 9))
            i--;
        
        end = i;  // Guarda el índice del final de la palabra

        // Mueve el índice hacia atrás hasta encontrar el inicio de la palabra
        while (i > 0 && SU_MENOS != 32 && SU_MENOS != 9)
            i--;
        
        start = i;  // Guarda el índice del inicio de la palabra

        // Imprime la palabra desde el inicio hasta el final
        while (start < end)
            write(1, &argv[1][start++], 1);
    }
    
    // Imprime una nueva línea al final para asegurar una salida limpia
    write(1, "\n", 1);
    return (0);  // Termina el programa exitosamente
}

/* 
#include <unistd.h>

#define SU_MENOS argv[1][i - 1]

int main(int argc, char **argv)
{
    int i = 0;
    int end = 0;
    int start = 0;

    if (argc == 2)
    {
        // Avanzar hasta el final de la cadena
        while (argv[1][i])
            i++;
        
        // Retroceder mientras haya espacios o tabulaciones
        while (i > 0 && (SU_MENOS == 32 || SU_MENOS == 9))
            i--;

        // Guardar el final de la última palabra
        end = i;

        // Retroceder hasta encontrar el inicio de la última palabra
        while (i > 0 && SU_MENOS != 32 && SU_MENOS != 9)
            i--;

        // Guardar el inicio de la última palabra
        start = i;

        // Imprimir la última palabra
        while (start < end)
            write(1, &argv[1][start++], 1);
    }

    write(1, "\n", 1);
    return 0;
} */
