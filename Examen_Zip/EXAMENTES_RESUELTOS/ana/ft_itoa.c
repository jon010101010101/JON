/*Escribe una función que tome un int y lo convierta en una cadena terminada en nulo.
La función devuelve el resultado en una matriz de caracteres que debes asignar.
Su función debe declararse de la siguiente manera:
char *ft_itoa(int nbr);
*/

/*
Truco para obtener el número max INT
un "int" esta formado por 32 bits
Positivos y negativos (enteros con signo): del -2147483648 al 2147483647

En un terminal ejecuta "bc"  (Basic Calculator)
pones 2 ^ 31 y obtienes 2147483648
para salir "quit"
*/
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int ft_len_num (int nbr)
{
	int count;
	
	count = 0;
	if (nbr == 0)
		count = 1;
	if (nbr < 0)
	{
		nbr = -nbr;
		count = 1;
	}
	while (nbr != 0)
	{
		nbr = nbr /10;
		count ++;
	}
	return (count);
}

char *ft_itoa(int nbr)
{
long num;
char *digits;
int len;
char *new_string;

num = nbr;
len  = ft_len_num(num);
digits = "0123456789";
new_string = (char *)malloc(sizeof(char) * (len + 1));
if (!new_string)
	return (NULL);
new_string[len] = '\0';
len = len -1;
if (num == 0)
	new_string[0] = '0';
if (num < 0)
{
	num = -num;
	new_string[0] = '-';
}
while (num != 0)
	{
	new_string[len] = digits[num % 10];
	num = num / 10;
	len--;
	}
return(new_string);
}

/*int main(void)
{
	char *itoa = ft_itoa(-2147483648);
	int i = 0;
	while (itoa[i])
	{
		write(1, &itoa[i], 1);
		i++;
	}
	write(1, "\n", 1);
}*/