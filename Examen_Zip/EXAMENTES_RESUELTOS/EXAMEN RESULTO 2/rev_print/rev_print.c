/*Escribe un programa que tome una cadena y la muestre al revés
seguido de una nueva línea.
Si el número de parámetros no es 1, el programa muestra una nueva línea.

Examples:
$> ./rev_print "zaz" | cat -e
zaz$
$> ./rev_print "dub0 a POIL" | cat -e
LIOP a 0bud$
$> ./rev_print | cat -e
$*/

/*JON BUENA*/

#include <unistd.h>
#include <string.h>

void print_reversed(const char *str)
{
    if (*str != '\0')
    {
        print_reversed(str + 1);
        write(1, str, 1);
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        print_reversed(argv[1]);
    }
    write(1, "\n", 1);
    return (0);
}

/* COMENTARIOS */

/* #include <unistd.h>   // Incluimos la biblioteca unistd.h para usar la función write
#include <string.h>   // Incluimos la biblioteca string.h para el manejo de cadenas

// Función recursiva para imprimir una cadena en orden inverso
void print_reversed(const char *str)
{
    // Verificamos si el carácter actual no es el terminador de cadena '\0'
    if (*str != '\0')
    {
        // Llamada recursiva con el siguiente carácter en la cadena
        print_reversed(str + 1);
        
        // Imprimimos el carácter actual en la salida estándar
        write(1, str, 1);
    }
}

int main(int argc, char **argv)
{
    // Verificamos que se ha pasado exactamente un argumento adicional al programa
    if (argc == 2)
    {
        // Llamamos a la función print_reversed con el primer argumento (cadena)
        print_reversed(argv[1]);
    }
    
    // Escribimos un salto de línea en la salida estándar después de imprimir la cadena
    write(1, "\n", 1);
    
    // Retornamos 0 para indicar que el programa terminó con éxito
    return (0);
} */

/* ANA */

#include <unistd.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
        i++;
    return (i);
}

int main(int argc, char **argv)
{
    int i;

    if (argc == 2)
    {
        i = ft_strlen(argv[1]) - 1;
        while (i >= 0)
        {
            write(1, &argv[1][i], 1);
            i--;
        }
    }
    write(1, "\n", 1);
    return (0);
}

/* COMENTARIOS ANA*/

/* #include <unistd.h>  // Incluimos la biblioteca unistd.h para usar la función write

// Función que calcula la longitud de una cadena
int ft_strlen(char *str)
{
    int i;  // Variable para contar los caracteres

    i = 0;  // Inicializamos el contador a 0
    // Iteramos sobre cada carácter de la cadena hasta encontrar el terminador nulo '\0'
    while (str[i] != '\0')
        i++;  // Incrementamos el contador
    // Devolvemos el tamaño de la cadena
    return (i);
}

int main(int argc, char **argv)
{
    int i;  // Variable para usar como índice

    // Verificamos que el programa recibió exactamente un argumento adicional
    if (argc == 2)
    {
        // Calculamos el índice del último carácter de la cadena (longitud - 1)
        i = ft_strlen(argv[1]) - 1;

        // Iteramos desde el final de la cadena hasta el principio
        while (i >= 0)
        {
            // Escribimos el carácter actual en la salida estándar
            write(1, &argv[1][i], 1);
            // Decrementamos el índice para pasar al carácter anterior
            i--;
        }
    }
    
    // Escribimos un salto de línea en la salida estándar después de imprimir la cadena
    write(1, "\n", 1);
    
    // Retornamos 0 para indicar que el programa terminó con éxito
    return (0);
} */


