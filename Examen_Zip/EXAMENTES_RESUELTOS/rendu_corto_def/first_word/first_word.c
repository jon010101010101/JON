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

#include <unistd.h>

#define SU argv[1][i]

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (SU == 32 || SU == 9)
			i++;
		while (SU >= 33 && SU <= 126)
		{
			write(1, &SU, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
