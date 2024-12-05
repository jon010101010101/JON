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


/* ANA */

#include <unistd.h>

int ft_strlen(char *str)
{
	int i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

int	main(int argc, char **argv)
{
	int len;
	
	if (argc == 2)
	{
		len = ft_strlen(argv[1]) - 1;
		while (len >= 0)
		{
			write(1, &argv[1][len], 1);
			len--;
		}
	}
	write(1, "\n", 1);
	return (0);
}

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int len = 0;

        // Encontrar la longitud de la cadena
        while (argv[1][len])
            len++;

        // Imprimir la cadena en reversa
        while (len > 0)
        {
            write(1, &argv[1][len - 1], 1);
            len--;
        }
    }
    write(1, "\n", 1); // Imprimir una nueva línea
    return 0;
}
