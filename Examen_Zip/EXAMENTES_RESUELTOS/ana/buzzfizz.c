/*Escribe un programa que imprima los números del 1 al 100, cada uno separado por un
nueva línea.
Si el número es múltiplo de 4, en su lugar imprime 'buzz'.
Si el número es múltiplo de 7, en su lugar imprime "fizz".
Si el número es múltiplo de 4 y múltiplo de 7, en su lugar imprime 'buzzfizz'.

Example:
$>./fizzbuzz
1
2
3
buzz
5
6
fizz
buzz
9
10
11
buzz
13
fizz
15
buzz
17
18
19
buzz
fizz
22
23
buzz
25
26
27
fizzbuzz
29
30
[...]
97
fizz
99
buzz
$> 
*/
#include <unistd.h>

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
		if (nbr % 28 == 0)
			write(1, "buzzfizz", 8);
		else if (nbr % 4 == 0)
			write(1, "buzz", 4);
		else if (nbr % 7 == 0)
			write(1, "fizz", 4);
		else ft_print_n (nbr);
		write (1, "\n", 1);
		nbr++;
	}
}