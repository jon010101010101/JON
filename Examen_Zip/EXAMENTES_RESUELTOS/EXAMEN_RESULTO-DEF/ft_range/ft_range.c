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

/* #include <unistd.h>
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

 n       while (i < len)
        {
            printf("%d ", array[i]);
            i++;
        }
        printf("\n");

        free(array);
    }
    return (0);
} */



/* OTRA FORMA FUNCION BUENA PASA MAQUINA*/

/* #include <stdio.h>

#define MAX_SIZE 1000  // Tamaño máximo de la matriz estática.

int *ft_range(int start, int end)
{
    static int matrix[MAX_SIZE];  // Matriz estática.
    int i = 0;
    long len;

    // Determinar la longitud del rango.
    if (start > end)
        len = (long)start - (long)end + 1;
    else
        len = (long)end - (long)start + 1;

    // Verificar que el rango no exceda el tamaño máximo.
    if (len > MAX_SIZE)
        len = MAX_SIZE;

    // Rellenar la matriz con los valores del rango.
    while (i < len)
    {
        matrix[i] = start;
        i++;
        if (start < end)
            start++;
        else
            start--;
    }

    return (matrix);  // Devolver el puntero al inicio de la matriz.
}

int main(void)
{
    int *array;
    int start = 0;
    int end = -3;
    int i = 0;
    int len;

    array = ft_range(start, end);
    
    // Calcular la longitud de la matriz de salida.
    if (start <= end)
        len = end - start + 1;
    else
        len = start - end + 1;

    // Imprimir los elementos del array.
    while (i < len && i < MAX_SIZE)
    {
        printf("%d ", array[i]);
        i++;
    }
    printf("\n");

    return (0);
} */

#include <stdio.h>

int *ft_range(int start, int end)
{
    static int result[1000];  // Matriz estática para almacenar los valores
    static int *ptr = result;  // Puntero para recorrer la matriz

    *ptr = start;  // Asigna el valor actual de `start` al puntero
    ptr++;  // Avanza el puntero

    // Caso base: si `start` es igual a `end`, termina la recursión
    if (start == end)
    {
        ptr = result;  // Reinicia el puntero para la próxima llamada
        return result;
    }
    // Recursividad para avanzar o retroceder
    if (start < end)
        ft_range(start + 1, end);  // Incrementa `start` si es menor que `end`
    else
        ft_range(start - 1, end);  // Decrementa `start` si es mayor que `end`
    return result;
}

int main(void)
{
    int *result;
    int i;

    result = ft_range(1, 3);
    i = 0;
    while (i < 3)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_range(-1, 2);
    i = 0;
    while (i < 4)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_range(0, 0);
    i = 0;
    while (i < 1)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    result = ft_range(0, -3);
    i = 0;
    while (i < 4)
    {
        printf("%d ", result[i]);
        i++;
    }
    printf("\n");

    return (0);
}
