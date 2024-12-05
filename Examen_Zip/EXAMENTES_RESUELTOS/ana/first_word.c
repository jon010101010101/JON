/*
Escribe un programa que tome una cadena y muestre su primera palabra, seguida 
de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o 
por el inicio/final de la cuerda.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

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
$>
*/
#include <unistd.h>

int ft_is_space(char c)
{
    return(c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc == 2)
    {
        while (argv[1][i] && ft_is_space(argv[1][i]))
            i++;
        while (argv[1][i] && !ft_is_space(argv[1][i]))
        {
            write(1, &argv[1][i], 1);
            i++;
        } 
    }
    write(1, "\n", 1);
    return (0);
    }