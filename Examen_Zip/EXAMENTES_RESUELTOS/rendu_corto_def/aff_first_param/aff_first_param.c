/*Escribe un programa que tome cadenas como argumentos y muestre su primer
argumento seguido de un \n.
Si el número de argumentos es menor que 1, el programa muestra \n.

Example:
$> ./aff_first_param vincent mit "l'ane" dans un pre et "s'en" vint | cat -e
vincent$
$> ./aff_first_param "j'aime le fromage de chevre" | cat -e
j'aime le fromage de chevre$
$> ./aff_first_param | cat -e
$*/

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>

int main (int argc, char **argv)
{
    int     i = 0;

    if (argc > 1)
    {
        while(argv[1][i] != '\0')
            write(1, &argv[1][i++], 1);
    }
    write(1, "\n", 1);
    return (0);
}