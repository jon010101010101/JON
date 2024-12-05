/*Assignment name  : expand_str
Expected files   : expand_str.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays it with exactly three spaces
between each word, with no spaces or tabs either at the beginning or the end,
followed by a newline.
A word is a section of string delimited either by spaces/tabs, or by the
start/end of the string.
If the number of parameters is not 1, or if there are no words, simply display
a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y la muestre exactamente con tres espacios.
entre cada palabra, sin espacios ni tabulaciones ni al principio ni al final,
seguido de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o por el
inicio/final de la cadena.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

Examples:
$> ./expand_str "vous   voyez   c'est   facile   d'afficher   la   meme   chose" | cat -e
vous   voyez   c'est   facile   d'afficher   la   meme   chose$
$> ./expand_str " seulement          la c'est      plus dur " | cat -e
seulement   la   c'est   plus   dur$
$> ./expand_str "comme c'est cocasse" "vous avez entendu, Mathilde ?" | cat -e
$
$> ./expand_str "" | cat -e
$
$>*/

/* es ok PASA MAQUINA*/
/* #include <unistd.h>

int	main(int argc, char **argv)
{
	int i = 0;
	int j = 0;
	if (argc == 2)
	{
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;
		while (argv[1][i])
		{
			if (argv[1][i] == ' ' || argv[1][i] == '\t')
				j = 1;
			if (!(argv[1][i] == ' ' || argv[1][i] == '\t'))
			{
				if (j)
					write(1, "   ", 3);
				j = 0;
				write(1, &argv[1][i], 1);
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
} */
/* ANA */

/* #include <unistd.h>

int ft_is_space(char c)
{
	return(c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
	int i;
	int j;

	i = 0;
	j = 0;
	if (argc == 2)
	{
		while (argv[1][i] && ft_is_space(argv[1][i]))
			i++;
		while (argv[1][i])
		{
			if (ft_is_space(argv[1][i]))
				j = 1;
			if (!ft_is_space(argv[1][i]))
			{
				if (j)
					write(1, "   ", 3);
				j = 0;
				write(1, &argv[1][i], 1);
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
} */

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc != 2)
	{
        write(1, "\n", 1);
        return 0;
    }

    char *str = argv[1];
    int in_word = 0; // Indicador para saber si estamos en una palabra
    int space_needed = 0; // Indicador para saber si necesitamos añadir espacios

    while (*str)
	{
        if (*str != ' ' && *str != '\t')
		{
            if (space_needed)
			{
                write(1, "   ", 3); // Imprimir tres espacios entre palabras
                space_needed = 0; // Reseteamos el indicador de espacio necesario
            }
            write(1, str, 1); // Imprimir el carácter
            in_word = 1; // Marcamos que estamos en una palabra
        }
		else if (in_word)
		{
            space_needed = 1; // Marcamos que necesitamos añadir espacios
            in_word = 0; // Marcamos que hemos salido de la palabra
        }
        str++;
    }

    write(1, "\n", 1); // Imprimir un salto de línea al final
    return 0;
}

