/*
Assignment name  : inter
Expected files   : inter.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in both strings, in the order they appear in the first
one.
The display will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en ambas cadenas, en el orden en que aparecen en la primera
uno.
La pantalla será seguida por un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Examples:
$>./inter "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
padinto$
$>./inter ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6ewg4$
$>./inter "rien" "cette phrase ne cache rien" | cat -e
rien$
$>./inter | cat -e
$
*/

/* ANA OK*/

/* #include <unistd.h>

int ft_not_seen_before(char *str, char c, int max_pos)
{
	int	i;

	i = 0;
	while (str[i] && (i < max_pos || max_pos == -1))
	{
		if (str[i] == c)
			return (0);
		else 
			i++;	
	}
	return (1);
}

int main (int argc, char **argv)
{
	int i;

	i = 0;
	if (argc == 3)
	{
		while (argv[1][i])
		{
			if (ft_not_seen_before(argv[1], argv[1][i], i) && !ft_not_seen_before(argv[2], argv[1][i], -1))
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
 */
/* COMENTARIOS */

/* #include <unistd.h>  // Incluye la biblioteca para la función write

// Esta función verifica si el carácter 'c' no se ha visto antes en la cadena 'str' 
// hasta la posición 'max_pos'. Devuelve 1 si 'c' no se ha visto antes, 0 si se ha visto.
int ft_not_seen_before(char *str, char c, int max_pos)
{
	int i;

	i = 0;
	// Recorre la cadena hasta que encuentra el carácter nulo '\0' o hasta la posición 'max_pos'
	// Si 'max_pos' es -1, recorre toda la cadena.
	while (str[i] && (i < max_pos || max_pos == -1))

    i < max_pos:
Esta condición es true mientras el índice i sea menor que max_pos. Si max_pos tiene un valor 
positivo, el bucle seguirá ejecutándose hasta que i alcance max_pos. Esto permite limitar el
 recorrido de la cadena hasta una posición específica.
max_pos == -1:
Si max_pos es -1, esta condición será true. Esto permite que el bucle recorra toda la cadena 
sin detenerse en una posición específica. Es decir, se ignora la restricción del valor de 
max_pos y el bucle solo se detendrá cuando llegue al final de la cadena (str[i] == '\0').
	{
		// Si encuentra el carácter 'c' antes de la posición 'max_pos', retorna 0 (visto antes).
		if (str[i] == c)
			return (0);
		else 
			i++;	
	}
	// Si no encuentra el carácter 'c', retorna 1 (no visto antes).
	return (1);
}

int main (int argc, char **argv)
{
	int i;

	i = 0;
	// Verifica si hay exactamente 3 argumentos (nombre del programa + 2 argumentos de usuario).
	if (argc == 3)
	{
		// Recorre cada carácter de la primera cadena (argv[1]).
		while (argv[1][i])
		{
			// Llama a 'ft_not_seen_before' para verificar:
			// 1. Si el carácter actual 'argv[1][i]' no se ha visto antes en 'argv[1]' hasta la posición 'i'.
			// 2. Si el carácter 'argv[1][i]' está presente en 'argv[2]'.
			if (ft_not_seen_before(argv[1], argv[1][i], i) && !ft_not_seen_before(argv[2], argv[1][i], -1))
				// Si ambas condiciones se cumplen, imprime el carácter único encontrado en ambas cadenas.
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	// Imprime una nueva línea al final.
	write(1, "\n", 1);
	return (0);
}
 */

#include <unistd.h>

int main(int argc, char **argv)
{
	
    if (argc != 3)
	{
        write(1, "\n", 1);
        return (0);
    }

    char seen[256] = {0}; // Arreglo para marcar caracteres ya vistos en ambas cadenas
    int i = 0, j;

    while (argv[1][i])
	{
        if (!seen[(unsigned char)argv[1][i]])
		{  // Si el carácter no ha sido visto
            j = 0;
            while (argv[2][j]) {
                if (argv[1][i] == argv[2][j])
				{  // Si el carácter está en ambas cadenas
                    write(1, &argv[1][i], 1);   // Mostrar el carácter
                    seen[(unsigned char)argv[1][i]] = 1; // Marcar como visto
                    break;
                }
                j++;
            }
        }
        i++;
    }

    write(1, "\n", 1);
    return 0;
}


