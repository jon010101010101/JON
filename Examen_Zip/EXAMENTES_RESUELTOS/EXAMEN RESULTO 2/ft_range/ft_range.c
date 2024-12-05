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

/* ANA */

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
int main(void)
{
    int *array;
    int start = 0;
    int end = -3;
    int i = 0;
    int len;

    array = ft_range(start, end);
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

/* MAIN COMPLETO QUE SACA LOS CASOS A LA VEZ */
/* int main(void)
{
    int *array;
    int start, end;
    int i, len;

    // Prueba 1: start <= end
    start = 1;
    end = 3;
    array = ft_range(start, end);
    if (array)
    {
        len = end - start + 1;
        printf("Range %d to %d: ", start, end);
        i = 0;
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

    // Prueba 2: start < end con valores negativos
    start = -1;
    end = 2;
    array = ft_range(start, end);
    if (array)
    {
        len = end - start + 1;
        printf("Range %d to %d: ", start, end);
        i = 0;
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

    // Prueba 3: start == end
    start = 0;
    end = 0;
    array = ft_range(start, end);
    if (array)
    {
        printf("Range %d to %d: ", start, end);
        printf("%d\n", array[0]);
        free(array);
    }
    else
    {
        printf("Error allocating memory.\n");
    }

    // Prueba 4: start > end con valores negativos
    start = 0;
    end = -3;
    array = ft_range(start, end);
    if (array)
    {
        len = start - end + 1;  // Ajuste correcto del cálculo de longitud
        printf("Range %d to %d: ", start, end);
        i = 0;
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

    return 0;
} */

/* COMENTARIOS */

/* #include <stdlib.h>  // Incluimos la biblioteca stdlib.h para poder usar la función malloc

// Definimos la función ft_range, que devuelve un puntero a un array de enteros
// La función toma dos enteros como argumentos: start (inicio) y end (fin)
int	*ft_range(int start, int end)
{
	long	i;   // Declaramos una variable i de tipo long que servirá como índice para el bucle
	long	len; // Declaramos una variable len de tipo long para almacenar la longitud del array

	// Calculamos la longitud del array en función de la relación entre start y end
	if (end > start)
		len = (long)end - (long)start + 1;  // Si end es mayor que start, la longitud es end - start + 1
	if (start > end)
		len = (long)start - (long)end + 1;  // Si start es mayor que end, la longitud es start - end + 1

	int *numbers;  // Declaramos un puntero a enteros para almacenar la dirección del array que se va a crear
	i = 0;  // Inicializamos i en 0

	// Asignamos memoria para el array de enteros, con un tamaño igual a la longitud calculada
	numbers = (int *)malloc(sizeof(int) * len);
	
	// Si la asignación de memoria falla (malloc devuelve NULL), retornamos NULL
	if (!numbers)
		return (NULL);
	
	// Llenamos el array con los valores desde start hasta end (o desde end hasta start)
	while (i < len)
	{
		if (start <= end)
			numbers[i++] = start++;  // Si start es menor o igual a end, llenamos el array incrementando start
		else
			numbers[i++] = start--;  // Si start es mayor que end, llenamos el array decrementando start
	}

	// Retornamos el puntero al array lleno
	return (numbers);
} */
/* IÑAKI */

/* #include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// IMPORTANTE Se "castea" a long los int porque el tamaño entre -2147483648 y 2147483647 es long
int *ft_range(int start, int end)           

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
    else                                        // Si start y end no son iguales
    {
        while (i < len)                         // Recorro el contador "i" mientras sea menor que el tamaño "len"
        {
            if (start > end)                    // Si start es mayor que end
                range[i++] = start--;           // Asigno start y le resto 1 aumento el contador "i" despues de asignar
            else
                range[i++] = start++;           // Asigno start y le sumo 1 aumento el contador "i" despues de asignar
        }
    }   
    return (range);
}
 */

/* 
int main(int argc, char **argv)
{
    int     *myrange;
    int     i;
    int     start;
    int     end;
    int     len;

    int     *numbers;
    numbers = ft_range(0, 0);
    printf("%d, ", numbers[0]);
    printf("%d, ", numbers[1]);
    printf("%d\n", numbers[2]);

    (void)argc;
    i = 0;
    start = atoi(argv[1]);
    end = atoi(argv[2]);
    if (start > end)
        len = start - end + 1;
    else
        len = end - start + 1;
    myrange = ft_range(start, end);
    printf("start %d end %d\n", start, end);
    while (i < len)
    {
        printf("%d, ", myrange[i]);
        i++;
    }     
    return (0);
}
*/



/* no esta bien */

/* #include <stdlib.h>

int	*ft_range(int start, int end)
{
	long	i;
	long len;
	
	if (end > start)
		len = (long)end - (long)start + 1;
	if (start> end)
		len = (long)start - (long)end + 1;

	int *numbers;
	i = 0;
	numbers = (int *)malloc(sizeof(int) * len);
	if (!numbers)
		return (NULL);
	
	while (i < len)
	{
		if (start <= end)
			numbers[i++] = start++;
		else
			numbers[i++] = start--;
	}
	return (numbers);
}


#include <stdio.h>

int	main(void)
{
    int start = -2;
    int end = 2;
    int start = -2147483648;
    int end = 2147483647;
    int *prueba = ft_range(start, end);
    int i = 0;
    while (i < 4)
 		printf("%d |", prueba[i++]);
    return (0);
} */
/* el anterior corregido */

/* #include <stdlib.h>
#include <stdio.h>
#include <limits.h>

int *ft_range(int start, int end)
{
    long i;
    long len;
    int *numbers;

    // Calcular el tamaño del array basándonos en la diferencia entre start y end
    if (end >= start)
        len = (long)end - (long)start + 1;
    else
        len = (long)start - (long)end + 1;

    // Verificar si la longitud calculada es válida y evitar overflow en malloc
    if (len > INT_MAX || len <= 0)
        return NULL;

    // Reservar memoria para el array
    numbers = (int *)malloc(sizeof(int) * len);
    if (!numbers)
        return NULL;

    // Llenar el array con la secuencia desde start hasta end
    i = 0;
    while (i < len)
    {
        if (start <= end)
            numbers[i++] = start++;
        else
            numbers[i++] = start--;
    }
    return numbers;
}

int main(void)
{
    int start = -2;
    int end = 2;

    // Nota: Este rango es extremadamente grande y puede causar un fallo de memoria
    // int start = -2147483648;
    // int end = 2147483647;

    int *prueba = ft_range(start, end);
    if (prueba == NULL)
    {
        printf("Error al asignar memoria o rango inválido.\n");
        return 1;
    }

    int len = end >= start ? end - start + 1 : start - end + 1;
    int i = 0;
    while (i < len)
        printf("%d |", prueba[i++]);

    // Liberar la memoria reservada
    free(prueba);

    return 0;
} */
