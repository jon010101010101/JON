#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// IMPORTANTE Se "castea" a long los int porque el tamaño entre -2147483648 y 2147483647 es long
int *ft_rrange(int start, int end)
{
    int     *range;
    long    len;
    int     i;

    i = 0;
    if (start > end)                            // Si start es mayor que end
        len = (long)start - (long)end + 1;      // "len" start - end + 1 (este "+ 1" es para que se incluya start y end)
                                                // Ejemplo 3 - 1 = 2 sin embargo falta por incluir un número 3,2,1 son "3"
    if (end > start)                            // Si end es mayor que start
        len = (long)end - (long)start + 1;
    range = (int *)malloc(sizeof(int) * len);   // reservo memoria para los 11 carácteres y el cierre
    if (!range)                                 // Protego el malloc
        return (NULL);
    if (start == end)                           // Si start y end son iguales
        range[i] = start;                       // Asigno start (o end) y paso a devorver, en el caso de los "int" no es necesario el cierre
    else
    {
        while (i < len)                         // Recorro el contador "i" mientras sea menor que el tamaño "len"
        {
            if (end > start)                    // Si end es mayor que start
                range[i++] = end--;             // Asigno end y le resto 1 aumento el contador "i" despues de asignar
            else
                range[i++] = end++;             // Asigno end y le sumo 1 aumento el contador "i" despues de asignar
        }
    }   
    return (range);
}

/* 
int main(void)
{
    int     *numbers;
    numbers = ft_range(0, 10);
    printf("%d, ", numbers[0]);
    printf("%d, ", numbers[1]);
    printf("%d\n", numbers[2]);

  
    return (0);
}
*/

/* 
int main(void)
{
    int     *numbers;
    numbers = ft_range(0, 10);
    printf("%d, ", numbers[0]);
    printf("%d, ", numbers[1]);
    printf("%d\n", numbers[2]);

  
    return (0);
}
*/

/*SANDRA BUENA*/
#include <stdlib.h>

int	*ft_rrange(int start, int end)
{
	long len;
	long	i = 0;
	int *numbers;

	if (end > start)
		len = (long)end - (long)start + 1;
	if (start > end)
		len = (long)start - (long)end + 1;
	numbers = (int *)malloc(sizeof(int) * len);
	if (!numbers)
		return (NULL);
	while (i < len)
	{
		if (start < end)
			numbers[i++] = end--;
		else
			numbers[i++] = end++;
	}
	return (numbers);
}

/*#include <stdio.h>
int	main(void)
{
 	int start = -2147483648;
    int end = 2147483647;
 	int *prueba = ft_rrange(start, end);
 	int i = 0;

 	while (i < 3)
 		printf("%d |", prueba[i++]);
	return (0);
}
*/

/*Assignment name  : ft_rrange
Expected files   : ft_rrange.c
Allowed functions: malloc
--------------------------------------------------------------------------------
Write the following function:
int     *ft_rrange(int start, int end);
It must allocate (with malloc()) an array of integers, fill it with consecutive
values that begin at end and end at start (Including start and end !), then
return a pointer to the first value of the array.
--------------------------------------------------------------------------------
Escribe la siguiente función:
int *ft_rrange(int start, int end);
Debe asignar (con malloc()) una matriz de números enteros, llenarla con números consecutivos
valores que comienzan al final y terminan al inicio (¡incluidos el inicio y el final!), luego
devuelve un puntero al primer valor de la matriz.

Examples:
- With (1, 3) you will return an array containing 3, 2 and 1
- With (-1, 2) you will return an array containing 2, 1, 0 and -1.
- With (0, 0) you will return an array containing 0.
- With (0, -3) you will return an array containing -3, -2, -1 and 0.*/