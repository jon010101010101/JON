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

/* #include <stdlib.h>
#include <stdio.h>

int *ft_rrange(int start, int end)
{
    long len;
    long i = 0;
    int *numbers;

    if (end >= start)
        len = (long)end - (long)start + 1;
    else
        len = (long)start - (long)end + 1;
    numbers = (int *)malloc(sizeof(int) * len);
    if (!numbers)
        return (NULL);
    if (start <= end)
    {
        while (i < len)
            numbers[i++] = end--;
    }
    else
    {
        while (i < len)
            numbers[i++] = end++;
    }

    return (numbers);
}

int main(void)
{
    int *array;
    int start = 0;
    int end = -3;
    int i = 0;
    int len;

    array = ft_rrange(start, end);
    if (array)
    {
        if (start <= end)
            len = end - start + 1;
        else
            len = start - end + 1;

        while (i < len)
        {
            printf("%d ", array[i]);
            i++;
        }
        printf("\n");
        free(array);
    }
    else
    {
        printf("Error allocating memory.\n");
    }
    return (0);
} */



/* ANA */

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
int main(void)
{
    int *array;
    int start = -1;
    int end = 2;
    int i = 0;
    int len;

    array = ft_rrange(start, end);
    if (array)
    {
        if (start <= end)
            len = end - start + 1;
        else
            len = start - end + 1;

        while (i < len)
        {
            printf("%d ", array[i]);
            i++;
        }
        printf("\n");
        free(array);
    }
    return (0);
}

/* COMENTARIOS */

/* #include <stdlib.h>  // Incluimos la biblioteca stdlib.h para usar la función malloc

// Definimos la función ft_rrange, que devuelve un puntero a un array de enteros
// La función toma dos enteros como argumentos: start (inicio) y end (fin)
int	*ft_rrange(int start, int end)
{
	long len;       // Declaramos una variable len de tipo long para almacenar la longitud del array
	long i = 0;     // Declaramos una variable i de tipo long que servirá como índice para el bucle
	int *numbers;   // Declaramos un puntero a enteros para almacenar la dirección del array que se va a crear

	// Calculamos la longitud del array en función de la relación entre start y end
	if (end > start)
		len = (long)end - (long)start + 1;  // Si end es mayor que start, la longitud es end - start + 1
	if (start > end)
		len = (long)start - (long)end + 1;  // Si start es mayor que end, la longitud es start - end + 1

	// Asignamos memoria para el array de enteros, con un tamaño igual a la longitud calculada
	numbers = (int *)malloc(sizeof(int) * len);

	// Si la asignación de memoria falla (malloc devuelve NULL), retornamos NULL
	if (!numbers)
		return (NULL);

	// Llenamos el array con los valores desde end hasta start (o desde start hasta end), en orden inverso
	while (i < len)
	{
		if (start < end)
			numbers[i++] = end--;  // Si start es menor que end, llenamos el array decrementando end
		else
			numbers[i++] = end++;  // Si start es mayor que end, llenamos el array incrementando end
	}

	// Retornamos el puntero al array lleno
	return (numbers);
} */
/* IÑAKI */
/* #include <unistd.h>
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
} */

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
