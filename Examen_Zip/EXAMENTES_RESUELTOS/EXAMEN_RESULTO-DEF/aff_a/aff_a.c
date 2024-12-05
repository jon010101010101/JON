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

#include <unistd.h>

int main(int argc, char **argv)
{
    int  i = 0;

    if(argc != 2)
        write(1, "a", 1);
    else
    {
        while(argv[1][i] != '\0')
        {
            if(argv[1][i] == 'a')
            {
                write(1, "a", 1);
                break ;
            }
            i++;
        }
    }
    write(1, "\n", 1);
    return (0);
}

/* COMENTARIOS */

/* #include <unistd.h>  // Biblioteca para usar la función write

int main(int argc, char **argv)
{
    int i = 0;  // Inicializamos el índice para recorrer la cadena

    // Verificar si el número de argumentos no es 2
    // Si no hay exactamente un argumento adicional, imprime 'a'
    if (argc != 2)
    {
        write(1, "a", 1);  // Imprime 'a' en la salida estándar (stdout)
    }
    else
    {
        // Recorremos el primer argumento (la cadena de entrada)
        while (argv[1][i] != '\0')
        {  // '\0' es el carácter nulo que indica el final de la cadena
            if (argv[1][i] == 'a')
            {  // Si encontramos el carácter 'a'
                write(1, "a", 1);  // Imprime 'a' en la salida estándar
                break;  // Termina el bucle cuando se encuentra la primera 'a'
            }
            i++;  // Incrementa el índice para verificar el siguiente carácter
        }
    }
    // Siempre imprime una nueva línea al final, independientemente del resultado anterior
    write(1, "\n", 1);

    return (0);  // El programa finaliza exitosamente
} */
