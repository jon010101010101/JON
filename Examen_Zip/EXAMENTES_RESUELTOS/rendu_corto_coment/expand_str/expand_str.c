/*Assignment name  : expand_str
Expected files   : expand_str.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays it with exactly three spaces
between each word, with no spaces or tabs either at the beginning or the end,
followed by a newline.
A word is a section of string delimited either by spaces/tabs, or by the
start/end of the string.
If the number of parameters is not 1, or if there are no words, simply display
a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y la muestre exactamente con tres espacios.
entre cada palabra, sin espacios ni tabulaciones ni al principio ni al final,
seguido de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o por el
inicio/final de la cadena.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

Examples:
$> ./expand_str "vous   voyez   c'est   facile   d'afficher   la   meme   chose" | cat -e
vous   voyez   c'est   facile   d'afficher   la   meme   chose$
$> ./expand_str " seulement          la c'est      plus dur " | cat -e
seulement   la   c'est   plus   dur$
$> ./expand_str "comme c'est cocasse" "vous avez entendu, Mathilde ?" | cat -e
$
$> ./expand_str "" | cat -e
$
$>*/

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h> // Incluye la biblioteca para usar la función write

#define SU argv[1][i] // Define un alias 'SU' para acceder al carácter actual de la cadena de argumentos

int main(int argc, char **argv)
{
    int i = 0; // Índice para recorrer la cadena de caracteres del argumento
    int j = 0; // Indicador de si hay espacios en blanco previos a una palabra

    // Verifica si se ha proporcionado exactamente un argumento adicional
    if (argc == 2)
    {
        // Avanza en la cadena saltando cualquier espacio en blanco inicial (' ' o '\t')
        while (SU == 32 || SU == 9)
            i++;
        
        // Recorre la cadena de caracteres del argumento hasta el final ('\0')
        while (SU)
        {
            // Si encuentra un espacio en blanco (' ' o '\t'), establece el indicador 'j' a 1
            if (SU == 32 || SU == 9)
                j = 1;

            // Si encuentra un carácter que no es un espacio en blanco
            if (!(SU == 32 || SU == 9))
            {
                // Si 'j' es 1, significa que había espacios antes de la palabra actual, imprime un solo espacio
                if (j)
                    write(1, "   ", 3); // Imprime un espacio como separador entre palabras
                j = 0; // Reinicia el indicador 'j' para el siguiente grupo de caracteres
                write(1, &SU, 1); // Imprime el carácter actual
            }
            i++; // Avanza al siguiente carácter en la cadena
        }
    }
    write(1, "\n", 1); // Imprime un salto de línea al final para asegurar que la salida sea legible
    return (0); // Retorna 0 para indicar que el programa ha finalizado correctamente
}

