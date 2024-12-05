/*Escribe un programa que imprima los números del 1 al 100, cada uno separado por un
nueva línea.
Si el número es múltiplo de 3, en su lugar imprime 'fizz'.
Si el número es múltiplo de 5, en su lugar imprime "buzz".
Si el número es múltiplo de 3 y múltiplo de 5, en su lugar imprime 'fizzbuzz'.

Example:
$>./fizzbuzz
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
[...]
97
98
fizz
buzz
$> 
*/

#include <unistd.h>

int ft_print_n(int nbr)
{
	char *digits;

	digits = "0123456789";
	if (nbr > 9)
		ft_print_n(nbr / 10);
	write(1, &digits[nbr % 10], 1);
	return (0);
}

int main (void)
{
	int nbr;

	nbr = 1;
	while (nbr <= 100)
	{
		if (nbr % 15 == 0)
			write(1, "fizzbuzz", 8);
		else if (nbr % 3 == 0)
			write(1, "fizz", 4);
		else if (nbr % 5 == 0)
			write(1, "buzz", 4);
		else ft_print_n (nbr);
		write (1, "\n", 1);
		nbr++;
	}
}