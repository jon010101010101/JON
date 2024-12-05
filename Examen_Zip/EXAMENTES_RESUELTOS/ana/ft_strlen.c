/*
Escribe una función que devuelva la longitud de una cadena.
Su función debe declararse de la siguiente manera:
int ft_strlen(char *str);
*/
#include <unistd.h>

int	ft_strlen(char *str)
{
	int i;

	i = 0;
	while(str[i])
		i++;
	return (i);
}