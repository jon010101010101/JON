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
$> ./last_word "   " | cat -e{{}}
$
$> ./last_word "a" "b" | cat -e
$
$> ./last_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>*/

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>

#define SU_M argv[1][i - 1]

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        int end = 0;
        int start = 0;
        
        while (argv[1][i])
            i++;

        while (i > 0 && (SU_M == 32 || SU_M == 9))
            i--;
        end = i;

        /* while (i > 0 && SU_M != 32 && SU_M != 9) */  /* alternativa */
        while (i > 0 && (SU_M >= 33 && SU_M <= 126))
            i--;
        start = i;
        while (start < end)
            write(1, &argv[1][start++], 1);
    }
    write(1, "\n", 1);
    return (0);
}
