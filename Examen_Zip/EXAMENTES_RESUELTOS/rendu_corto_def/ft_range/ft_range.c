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

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_range(int start, int end)
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

    // Llenar el array con los valores en el rango
    while (i < len)
    {
        matrix[i] = start; // Asignar el valor de 'start' al array
        if (start > end)
            start--;
        else
            start++;
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

    result = ft_range(start, end);
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

/* int main(void)
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
} */

/* VERSION ALTERNATIVO, FUNCIONA PERO NO PASA MAQUINA */

/* #include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int *ft_range(int start, int end)
{
    static int result[100];
    static int *ptr = result;

    *ptr = start;
    ptr++;

    if (start == end)
	{
        ptr = result;
        return (result);
    }
    if (start < end)
	    ft_range(start + 1, end);
	else
        ft_range(start - 1, end);
    return (result);
} */


 