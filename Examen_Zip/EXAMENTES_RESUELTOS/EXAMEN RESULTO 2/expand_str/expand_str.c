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

/* es ok */
#include <unistd.h>

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
}
/* COMENTARIOS */

/* #include <unistd.h>

int	main(int argc, char **argv)
{
	int i = 0;
	int j = 0;

	// Verifica si se pasó exactamente un argumento
	if (argc == 2)
	{
		// Salta los espacios y tabulaciones al inicio de la cadena
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;

		// Recorre el resto de la cadena
		while (argv[1][i])
		{
			// Verifica si el carácter actual es un espacio o tabulación
			if (argv[1][i] == ' ' || argv[1][i] == '\t')
				j = 1;  // Marca que se ha encontrado un espacio/tabulación

			// Si el carácter no es un espacio o tabulación
			if (!(argv[1][i] == ' ' || argv[1][i] == '\t'))
			{
				// Si se encontró un espacio/tabulación antes, imprime tres espacios
				if (j)
					write(1, "   ", 3);

				// Restablece la marca de espacio/tabulación
				j = 0;

				// Imprime el carácter actual
				write(1, &argv[1][i], 1);
			}
			i++;
		}
	}

	// Imprime una nueva línea al final
	write(1, "\n", 1);

	return (0);
} */


/* ANA */
/* #include <unistd.h>

int	ft_is_space(char c)
{
	return (c == ' ' || c == '\t');
}

int	main(int argc, char **argv)
{
	int	i;
	int	j;

	i = 0;
	j = 0;

	if (argc == 2)
	{
		if (ft_is_space(argv[1][i]))
			i++;
		while (argv[1][i])
		{
			if (ft_is_space(argv[1][i]))
				j = 1;
			if (!ft_is_space(argv[1][i]))
			{
				if (j)
				{
					write(1, "   ", 3); ERROR ANA QUE TIENE TRES X CUANDO ES ESPACIO
					j = 0;
				}
				write(1, &argv[1][i], 1);
			}
		i++;
		}	
	}
	write(1, "\n", 1);
	return (0);
} */
/* COMENTARIOS */

/* #include <unistd.h>  // Incluimos la biblioteca unistd.h para poder usar la función write

int	main(int argc, char **argv)  // La función main, que recibe el número de argumentos (argc) y un array de strings (argv)
{
	int i = 0;  // Declaramos la variable i, que se utilizará como índice para recorrer la cadena
	int j = 0;  // Declaramos la variable j, que se usará como flag (bandera) para saber si se ha encontrado un espacio o tabulación

	if (argc == 2)  // Verificamos si hay exactamente dos argumentos (el nombre del programa y un argumento adicional)
	{
		// Este bucle ignora los espacios y tabulaciones al inicio de la cadena
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;

		// Este bucle principal recorre la cadena hasta el final
		while (argv[1][i])
		{
			// Si encontramos un espacio o una tabulación, activamos la bandera j
			if (argv[1][i] == ' ' || argv[1][i] == '\t')
				j = 1;

			// Si el carácter actual no es un espacio ni una tabulación
			if (!(argv[1][i] == ' ' || argv[1][i] == '\t'))
			{
				// Si j está activado, significa que hemos encontrado un espacio o tabulación antes,
				// así que imprimimos tres espacios antes de continuar con la palabra actual
				if (j)
					write(1, "   ", 3);

				j = 0;  // Desactivamos la bandera j ya que estamos dentro de una palabra
				write(1, &argv[1][i], 1);  // Escribimos el carácter actual en la salida estándar
			}

			i++;  // Avanzamos al siguiente carácter en la cadena
		}
	}

	write(1, "\n", 1);  // Al final, imprimimos un salto de línea
	return (0);  // Devolvemos 0 para indicar que el programa terminó correctamente
} */