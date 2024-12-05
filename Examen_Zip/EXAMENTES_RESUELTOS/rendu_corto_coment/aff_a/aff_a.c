/*
Assignment name  : aff_a
Expected files   : aff_a.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string, and displays the first 'a' 
character it encounters in it, followed by a newline. If there are no 
'a' characters in the string, the program just writes a newline. 
If the number of parameters is not 1, the program displays 'a' 
followed by a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y muestre la primera 'a'
carácter que encuentra en él, seguido de una nueva línea. si no hay
caracteres 'a' en la cadena, el programa simplemente escribe una nueva línea.
Si el número de parámetros no es 1, el programa muestra 'a'
seguido de una nueva línea.

Example:
$> ./aff_a "abc" | cat -e
a$
$> ./aff_a "dubO a POIL" | cat -e
a$
$> ./aff_a "zz sent le poney" | cat -e
$
$> ./aff_a | cat -e
a$
*/

#include <unistd.h> // Incluye la biblioteca para usar la función write

int main(int argc, char **argv)
{
    int i = 0; // Declaración e inicialización del índice para recorrer la cadena de caracteres

    // Verifica si el número de argumentos es diferente de 2
    // Si no se pasa exactamente un argumento (además del nombre del programa)
    if(argc != 2)
        write(1, "a", 1); // Imprime 'a' en la salida estándar
    else
    {
        // Recorre cada carácter del argumento pasado hasta encontrar el final de la cadena
        while(argv[1][i] != '\0')
        {
            // Verifica si el carácter actual es 'a'
            if(argv[1][i] == 'a')
            {
                write(1, "a", 1); // Imprime 'a' en la salida estándar
                break ; // Detiene el bucle después de encontrar la primera 'a'
            }
            i++; // Incrementa el índice para verificar el siguiente carácter
        }
    }
    // Imprime un salto de línea al final para asegurar que la salida sea legible en la consola
    write(1, "\n", 1);

    return (0); // Retorna 0 para indicar que el programa ha finalizado correctamente
}

