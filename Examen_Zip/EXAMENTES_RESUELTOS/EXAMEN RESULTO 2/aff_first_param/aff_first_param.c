/*Escribe un programa que tome cadenas como argumentos y muestre su primer
argumento seguido de un \n.
Si el número de argumentos es menor que 1, el programa muestra \n.

Example:
$> ./aff_first_param vincent mit "l'ane" dans un pre et "s'en" vint | cat -e
vincent$
$> ./aff_first_param "j'aime le fromage de chevre" | cat -e
j'aime le fromage de chevre$
$> ./aff_first_param | cat -e
$*/

#include <unistd.h>

int main (int argc, char **argv)
{
    int     i = 0;

    if (argc > 1)
    {
        while(argv[1][i] != '\0')
            write(1, &argv[1][i++], 1);
    }
    write(1, "\n", 1);
    return (0);
}

/* #include <unistd.h>  // Incluye la biblioteca que proporciona la función 'write'.

int main (int argc, char **argv)
{
    int i = 0;  // Inicializa el índice 'i' para recorrer la cadena de caracteres.

    // Verifica si hay más de un argumento (es decir, al menos un argumento adicional al nombre del programa).
    if (argc > 1)
    {
        // Mientras el carácter actual no sea el carácter nulo '\0' (es decir, no se haya llegado al final de la cadena).
        while (argv[1][i] != '\0')
        {
            // Escribe el carácter actual en la salida estándar (generalmente la consola).
            // &argv[1][i] es un puntero al carácter actual.
            // i++ incrementa 'i' para pasar al siguiente carácter en la próxima iteración.
            write(1, &argv[1][i++], 1);
        }
    }
    // Escribe un salto de línea en la salida estándar para asegurar que la salida termine con una nueva línea.
    write(1, "\n", 1);
    return (0);  // Devuelve 0 para indicar que el programa terminó correctamente.
} */


