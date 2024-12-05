/*Escribe la siguiente función:
int *ft_range(int start, int end);
Debe asignar (con malloc()) una matriz de números enteros, llenarla con números consecutivos
valores que comienzan al principio y terminan al final (¡incluidos el inicio y el final!), luego
devuelve un puntero al primer valor de la matriz.

Examples:
- With (1, 3) you will return an array containing 1, 2 and 3.
- With (-1, 2) you will return an array containing -1, 0, 1 and 2.
- With (0, 0) you will return an array containing 0.
- With (0, -3) you will return an array containing 0, -1, -2 and -3.
*/
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_range(int start, int end)
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
			matrix[i] = start;
			i++;
			start++;
		}
		else 
	
		{
			matrix[i] = start;
			i++;
			start--;
		}
	}
	return(matrix);

}

/*int main (void)
{
	int i = 0;
	int *matrix = ft_range (1, 10);
	while (matrix[i])
	{
		printf("%d", matrix[i]);
		i++;
	}
	return (0);
}*/
