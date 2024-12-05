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

/* ANA */

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
} */

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

/* OTRA FORMA FUNCIONA */

/* #include <stdio.h>

#define MAX_SIZE 1000  // Definir un tamaño máximo para la matriz estática.

// Función para generar un rango de números enteros desde 'start' hasta 'end' en orden inverso.
int *ft_rrange(int start, int end)
{
    static int matrix[MAX_SIZE];  // Matriz estática de tamaño fijo.
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

    // Rellenar la matriz en orden inverso.
    if (start <= end)
    {
        // Inicializar al final del rango e ir decreciendo.
        start += len - 1;
        while (i < len)
        {
            matrix[i] = start;
            i++;
            start--;
        }
    }
    else
    {
        // Inicializar al final del rango e ir decreciendo.
        end += len - 1;
        while (i < len)
        {
            matrix[i] = end;
            i++;
            end--;
        }
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

    array = ft_rrange(start, end);

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

int *ft_rrange(int start, int end)
{
    static int result[100];  // Matriz estática con un tamaño fijo
    static int *ptr = result;  // Puntero estático para mantener la posición actual en la matriz

    // Asigna el valor actual de `end` y luego avanza el puntero
    *ptr = end;
    ptr++;
    // Condición base: si `end` es igual a `start`, restablecemos el puntero y retornamos el resultado
    if (end == start)
	{
        ptr = result;  // Reinicia el puntero para futuras llamadas
        return (result);
    }
    // Llamada recursiva para llenar el resto del arreglo
    if (start < end)
	        ft_rrange(start, end - 1);  // Disminuye `end` si `start` es menor
    else
        ft_rrange(start, end + 1);  // Aumenta `end` si `start` es mayor
    return (result);
}

int main()
{
    int *result;

    // Ejemplos de prueba
    result = ft_rrange(1, 3);
    for (int i = 0; i < 3; i++)
        printf("%d ", result[i]);
    printf("\n");

    result = ft_rrange(-1, 2);
    for (int i = 0; i < 4; i++)
        printf("%d ", result[i]);
    printf("\n");

    result = ft_rrange(0, 0);
    for (int i = 0; i < 1; i++)
        printf("%d ", result[i]);
    printf("\n");

    result = ft_rrange(0, -3);
    for (int i = 0; i < 4; i++)
        printf("%d ", result[i]);
    printf("\n");

    return (0);
}

