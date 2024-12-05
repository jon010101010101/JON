/*Escribe un programa que tome un string y muestre el primer cáracter 'a'
que encuentre en él, seguido de una nueva línea. si no hay
caracteres 'a' en el string, el programa simplemente escribe una nueva línea.
Si el número de parámetros no es 1, el programa muestra 'a'
seguido de una nueva línea.

Example:
$> ./aff_a "abc" | cat -e
a$
$> ./aff_a "dubO a POIL" | cat -e
a$
$> ./aff_a "zz sent le poney" | cat -e
$
$> ./aff_a | cat -e
a$
*/
#include <unistd.h>

int main(int argc, char **argv)
{
	int	i;
	
	i =0;
	if (argc !=2)
	{
		write(1, "a", 1);
		write(1, "\n", 1);
		return (0);
	}
	while (argv[1][i])
	{
		if (argv[1][i] == 'a')
		{
			write(1, "a", 1);
			break;
		}
		i++;
	}
	write(1, "\n", 1);
	return (0);
}
