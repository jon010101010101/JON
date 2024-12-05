/*
Assignment name  : union
Expected files   : union.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in either one of the strings.
The display will be in the order characters appear in the command line, and
will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en cualquiera de las cadenas.
La pantalla se mostrará en el orden en que aparecen los caracteres en la línea 
de comando y irá seguido de un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Example:
$>./union zpadinton "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
zpadintoqefwjy$
$>./union ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6vewg4thras$
$>./union "rien" "cette phrase ne cache rien" | cat -e
rienct phas$
$>./union | cat -e
$
$>
$>./union "rien" | cat -e
$
$>
*/

#include <unistd.h>  // Incluye la biblioteca estándar para usar la función write

#define SU argv[1][i]  // Define un alias 'SU' para el carácter actual en argv[1] en el índice i
#define SU2 argv[2][j]  // Define un alias 'SU2' para el carácter actual en argv[2] en el índice j

int main(int argc, char **argv)
{
    // Verifica que se hayan proporcionado exactamente dos argumentos
    if (argc != 3)
    {
        write(1, "\n", 1);  // Si no se cumplen los requisitos, imprime una nueva línea y termina el programa
        return (0);
    }

    // Tamaño máximo del array para marcar caracteres ya vistos (256 para incluir todos los posibles caracteres ASCII)
    char seen[256] = {0};  // Array para marcar caracteres que ya han sido vistos en las cadenas
    int i = 0;  // Índice para recorrer el primer argumento
    int j = 0;  // Índice para recorrer el segundo argumento

    // Recorre cada carácter en el primer argumento (argv[1])
    while (SU)
    {
        // Si el carácter no ha sido visto antes (según el array 'seen')
        if (!seen[(unsigned char)SU])
        {
            seen[(unsigned char)SU] = 1;  // Marca el carácter como visto en el array 'seen'
            write(1, &SU, 1);  // Imprime el carácter en la salida estándar
        }
        i++;  // Avanza al siguiente carácter en argv[1]
    }

    // Recorre cada carácter en el segundo argumento (argv[2])
    while (SU2)
    {
        // Si el carácter no ha sido visto antes (según el array 'seen')
        if (!seen[(unsigned char)SU2])
        {
            seen[(unsigned char)SU2] = 1;  // Marca el carácter como visto en el array 'seen'
            write(1, &SU2, 1);  // Imprime el carácter en la salida estándar
        }
        j++;  // Avanza al siguiente carácter en argv[2]
    }

    write(1, "\n", 1);  // Imprime una nueva línea después de procesar ambos argumentos
    return (0);  // Termina el programa exitosamente
}
