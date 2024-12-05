/*Escribe un programa que tome dos cadenas y muestre, sin dobles, el
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
#include <unistd.h>

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