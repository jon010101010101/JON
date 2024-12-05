/*Escribe una función que muestre una cadena en la salida estándar.
El puntero pasado a la función contiene la dirección del primer caracter de la
cadena.
Su función debe declararse de la siguiente manera:
void ft_putstr(char *str);
*/
#include <unistd.h>

void	ft_putstr(char *str)
{
	int i;

	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
}