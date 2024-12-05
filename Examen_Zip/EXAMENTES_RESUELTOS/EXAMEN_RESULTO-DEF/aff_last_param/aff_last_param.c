/*Assignment name  : aff_last_param
Expected files   : aff_last_param.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes strings as arguments, and displays its last
argument followed by a newline.
If the number of arguments is less than 1, the program displays a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome cadenas como argumentos y muestre su último
argumento seguido de una nueva línea.
Si el número de argumentos es menor que 1, el programa muestra una nueva línea.

Examples:
$> ./aff_last_param "zaz" "mange" "des" "chats" | cat -e
chats$
$> ./aff_last_param "j'aime le savon" | cat -e
j'aime le savon$
$> ./aff_last_param | cat -e
$*/

#include <unistd.h>

int main(int argc, char **argv)
{
    int  i = 0;

    if (argc >1)
    {
        while (argv[argc-1][i] != '\0')
            write(1, &argv[argc - 1][i++], 1); 
    }
    write(1, "\n", 1);
    return (0);
}

/* #include <unistd.h>  // Incluye la biblioteca que proporciona la función 'write'.

int main(int argc, char **argv)
{
    int i = 0;  // Inicializa el índice 'i' para recorrer la cadena de caracteres.

    // Verifica si hay más de un argumento (es decir, al menos un argumento adicional al nombre del programa).
    if (argc > 1)
    {
        // Mientras el carácter actual en la cadena del último argumento no sea el carácter nulo '\0' (es decir, no se haya llegado al final de la cadena).
        while (argv[argc - 1][i] != '\0')
        {
            // Escribe el carácter actual en la salida estándar (generalmente la consola).
            // &argv[argc - 1][i] es un puntero al carácter actual.
            // i++ incrementa 'i' para pasar al siguiente carácter en la próxima iteración.
            write(1, &argv[argc - 1][i++], 1); 
        }
    }
    // Escribe un salto de línea en la salida estándar para asegurar que la salida termine con una nueva línea.
    write(1, "\n", 1);
    return (0);  // Devuelve 0 para indicar que el programa terminó correctamente.
} */

