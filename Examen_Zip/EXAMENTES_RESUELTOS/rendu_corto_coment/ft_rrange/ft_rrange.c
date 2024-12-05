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

#include <unistd.h>  // Incluye la biblioteca estándar para usar funciones del sistema
#include <stdlib.h>  // Incluye la biblioteca estándar para usar malloc y funciones de gestión de memoria
#include <stdio.h>   // Incluye la biblioteca estándar para usar funciones de entrada/salida (útil para pruebas)

int *ft_rrange(int start, int end)
{
    int i;            // Variable para el índice de la matriz
    long len;         // Longitud de la matriz a crear
    int *matrix;      // Puntero a la matriz que contendrá los números del rango

    i = 0;  // Inicializa el índice a 0

    // Calcula la longitud del rango en función de los valores de 'start' y 'end'
    if (start > end)
        len = (long)start - (long)end + 1;  // Si 'start' es mayor, longitud es la diferencia más uno
    if (start < end)
        len = (long)end - (long)start + 1;  // Si 'end' es mayor, longitud es la diferencia más uno
    if (start == end)
        len = 1;  // Si son iguales, la longitud es 1 (sólo un elemento)

    // Reserva memoria para la matriz de enteros con el tamaño calculado
    matrix = (int *)malloc(sizeof(int) * len);
    if (!matrix)  // Verifica si la asignación de memoria falló
        return (NULL);

    // Llena la matriz con los números en el rango de 'end' a 'start'
    while (i < len)
    {
        if (end >= start)  // Si 'end' es mayor o igual a 'start'
        {
            matrix[i] = end;  // Asigna el valor de 'end' a la matriz
            i++;              // Incrementa el índice
            end--;            // Decrementa 'end' para el siguiente valor
        }
        else  // Si 'start' es mayor que 'end'
        {
            matrix[i] = end;  // Asigna el valor de 'end' a la matriz
            i++;              // Incrementa el índice
            end++;            // Incrementa 'end' para el siguiente valor
        }
    }
    return (matrix);  // Retorna el puntero a la matriz con el rango creado
}



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
        return result;
    }
    if (start < end)
	{
        ft_rrange(start, end - 1);
    }
	else
	{
        ft_rrange(start, end + 1);
    }
    return (result);
} */

/* int main(void)
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
} */
