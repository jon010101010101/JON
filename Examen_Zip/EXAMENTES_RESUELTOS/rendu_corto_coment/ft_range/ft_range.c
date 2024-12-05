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

#include <unistd.h>  // Librería estándar para funciones del sistema operativo, como escribir en la consola
#include <stdlib.h>  // Librería estándar para funciones de memoria dinámica, como malloc
#include <stdio.h>   // Librería estándar para funciones de entrada/salida, como printf

// Función que genera un rango de números desde 'start' hasta 'end' y devuelve un puntero a un array con los números
int *ft_range(int start, int end)
{
    int len;          // Variable para almacenar la longitud del rango
    int *matrix;      // Puntero para almacenar la dirección de memoria del array dinámico
    int i = 0;        // Variable de control para el bucle

    // Calcula la longitud del rango
    if (start > end)
        len = start - end + 1;  // Si el inicio es mayor que el final, la longitud es la diferencia más uno
    else
        len = end - start + 1;  // Si el final es mayor o igual que el inicio, la longitud es la diferencia más uno
    
    // Asigna memoria para el array dinámico
    matrix = (int *)malloc(sizeof(int) * len);  // Asigna memoria para 'len' elementos de tipo 'int'
    if (!matrix)                                // Verifica si la asignación de memoria fue exitosa
        return (NULL);                          // Si no, retorna NULL
    
    // Rellena el array con los valores desde 'start' hasta 'end'
    while (i < len)
    {
        matrix[i] = start;    // Asigna el valor actual de 'start' al array
        if (start > end)      // Si 'start' es mayor que 'end', decrementa 'start'
            start--;
        else                  // Si 'start' es menor o igual que 'end', 
                                // incrementa 'start'
            start++;
        i++;                  // Incrementa el índice
    }
    
    return (matrix);            // Retorna el puntero al array lleno
}
#include <stdio.h>

int main (void)
{
    int *result;
    int start = -1;
    int end = 2;
    int i = 0;
    int len;

    if(start > end)
        len = start -end + 1;
    else
        len = end - start + 1;

    result = ft_range(start, end);

    while (i < len)
    {
        printf("%d\n ", result[i]);
        i++;
    }
    return(0);
}
 /* main con todos los casos */
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


/* #include <stdio.h>

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

