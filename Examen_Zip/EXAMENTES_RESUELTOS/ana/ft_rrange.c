/*Escribe la siguiente función:
int *ft_rrange(int start, int end);
Debe asignar (con malloc()) una matriz de números enteros, llenarla con números consecutivos
valores que comienzan al final y terminan al inicio (¡incluidos el inicio y el final!), luego
devuelve un puntero al primer valor de la matriz.

Examples:
- With (1, 3) you will return an array containing 3, 2 and 1
- With (-1, 2) you will return an array containing 2, 1, 0 and -1.
- With (0, 0) you will return an array containing 0.
- With (0, -3) you will return an array containing -3, -2, -1 and 0.
*/
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_rrange(int start, int end)
{
	int i;
	long len;
	int	*matrix;

	i = 0;
	if (start > end)
		len = (long)start - (long)end + 1;
	if (start < end)
		len = (long)end - (long)start + 1;
	if (start == end)
		len = 1;
	matrix = (int *)malloc(sizeof(int) * (len));
	if (!matrix)
		return (NULL);
	while (i < len)
	{
		if (end >= start)
		{
			matrix[i] = end;
			i++;
			end--;
		}
		else 
	
		{
			matrix[i] = end;
			i++;
			end++;
		}
	}
	return(matrix);
}
/*int main (void)
{
	int i = 0;
	int *matrix = ft_rrange (1, 10);
	while (matrix[i])
	{
		printf("%d", matrix[i]);
		i++;
	}
	return (0);
}*/
