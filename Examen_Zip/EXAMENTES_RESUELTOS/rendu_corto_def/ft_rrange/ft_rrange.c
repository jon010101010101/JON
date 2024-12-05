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
/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_rrange(int start, int end)
{
    int len;
    int *matrix;
    int i = 0;

    // Calcular la longitud del rango
    if (start > end)
        len = start - end + 1;
    else
        len = end - start + 1;

    // Asignar memoria para el rango
    matrix = (int *)malloc(sizeof(int) * len);
    if (!matrix)
        return (NULL);

    // Llenar el rango en orden inverso
    while (i < len)
    {
        matrix[i] = end; // Asignar el valor de 'end' al array
        if (start > end)
            end++;
        else
            end--;
        i++;
    }
    return (matrix);
}
/* PROBAR DE UNO EN UNO. FUNCIONA SIN LO COMENTADO*/

int main(void)
{
    int start = -1;
    int end = 2;
    int len;
    int *result;
    int i = 0;

    if (start > end)
        len = start - end + 1;
    else
        len = end - start + 1; 

    result = ft_rrange(start, end);
/*     if (!result)
    {
        printf("Memory allocation failed\n");
        return (1);
    } */
    while (i < len)
    {
        printf("%d ", result[i]);
        i++;
    }
    /* printf("\n");
    free(result); */
    return (0);
}
/* TODAS LAS PRUEBAS A LA VEZ */

int main(void)
{
    int *result;
    int i;

    result = ft_rrange(1, 3);
    i = 0;
    while (i < 3)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_rrange(-1, 2);
    i = 0;
    while (i < 4)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_rrange(0, 0);
    i = 0; 
    while (i < 1)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_rrange(0, -3);
    i = 0;
    while (i < 4)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    return (0);
}


/* ANA FUNCIONA Y PASA MAQUINA */

/* #include <unistd.h>
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
		if (end >= start) // Si 'end' es mayor o igual a 'start'
		{
			matrix[i] = end;
			i++;
			end--;
		}
		else // Si 'start' es mayor que 'end'
		{
			matrix[i] = end;
			i++;
			end++;
		}
	}
	return(matrix);
} */

/* FUNCIONA PERO NO PASA MAQUINA */
/* #include <stdio.h>

int *ft_rrange(int start, int end)
{
    static int result[100];
    static int *ptr = result;

    *ptr = end;
    ptr++;

    if (end == start)
	{
        ptr = result;
        return (result);
    }
    if (start < end)
        ft_rrange(start, end - 1);
	else
        ft_rrange(start, end + 1);
    return (result);
} */

