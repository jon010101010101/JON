/*
Assignment name  : inter
Expected files   : inter.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in both strings, in the order they appear in the first
one.
The display will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en ambas cadenas, en el orden en que aparecen en la primera
uno.
La pantalla será seguida por un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Examples:
$>./inter "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
padinto$
$>./inter ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6ewg4$
$>./inter "rien" "cette phrase ne cache rien" | cat -e
rien$
$>./inter | cat -e
$
*/

#include <unistd.h>  // Incluye la biblioteca estándar para usar la función write

#define SU argv[1][i]  // Define un alias 'SU' para acceder al carácter actual en el primer argumento
#define SU2 argv[2][j] // Define un alias 'SU2' para acceder al carácter actual en el segundo argumento

int main(int argc, char **argv)
{
    // Verifica que se han proporcionado exactamente dos argumentos adicionales
    if (argc != 3)
    {
        write(1, "\n", 1);  // Imprime una nueva línea si no se cumplen las condiciones
        return (0);         // Finaliza el programa
    }

    // Define un array para marcar los caracteres que ya han sido vistos
    // Tamaño 256 (255 + O)para cubrir todos los posibles valores de caracteres ASCII
    char seen[256] = {0};
    int i = 0;  // Índice para recorrer el primer argumento
    int j;      // Índice para recorrer el segundo argumento

    // Recorre cada carácter del primer argumento
    while (SU)
    {
        // Verifica si el carácter actual no ha sido marcado como visto
        if (!seen[(unsigned char)SU]) //(*)
        {
            j = 0;  // Inicializa el índice para recorrer el segundo argumento
            // Recorre cada carácter del segundo argumento
            while (SU2)
            {
                // Si el carácter actual del primer argumento se encuentra en el segundo argumento
                if (SU == SU2)
                {
                    write(1, &SU, 1);    // Imprime el carácter encontrado
                    seen[(unsigned char)SU] = 1; // Marca el carácter como visto
                    break;  // Sale del bucle interior para evitar imprimir caracteres duplicados
                }
                j++;  // Avanza al siguiente carácter en el segundo argumento
            }
        }
        i++;  // Avanza al siguiente carácter en el primer argumento
    }
    write(1, "\n", 1);  // Imprime una nueva línea al final de la salida
    return (0);  // Finaliza el programa correctamente
}

/* (*) Al convertir SU a (unsigned char), te aseguras de que el carácter se interprete como un valor sin signo de 0 a 255. 
Esto es importante porque el array seen tiene un tamaño de 256 elemento */
