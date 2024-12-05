/*Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en cualquiera de las cadenas.
La pantalla se mostrará en el orden en que aparecen los caracteres en la línea 
de comando y irá seguido de un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Example:
$>./union zpadinton "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
zpadintoqefwjy$
$>./union ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6vewg4thras$
$>./union "rien" "cette phrase ne cache rien" | cat -e
rienct phas$
$>./union | cat -e
$
$>
$>./union "rien" | cat -e
$
$>
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
	int j;

	i = 0;
	j = 0;
	if (argc == 3)
	{
		while (argv[1][i])
		{
			if (ft_not_seen_before(argv[1], argv[1][i], i))
				write(1, &argv[1][i], 1);
			i++;
		}
		while (argv[2][j])
		{
			if (ft_not_seen_before(argv[2], argv[2][j], j) && ft_not_seen_before(argv[1], argv[2][j], -1))
				write(1, &argv[2][j], 1);
			j++;
		}
	}
	write(1, "\n", 1);
	return (0);
}