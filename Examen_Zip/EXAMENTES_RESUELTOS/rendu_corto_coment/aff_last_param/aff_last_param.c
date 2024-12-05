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

#include <unistd.h> // Incluye la biblioteca para usar la función write

int main(int argc, char **argv)
{
    int i = 0; // Declaración e inicialización del índice para recorrer la cadena de caracteres

    // Verifica si se ha proporcionado al menos un argumento adicional
    if (argc > 1)
    {
        // Recorre la cadena del último argumento proporcionado al programa
        // (argv[argc - 1]) hasta encontrar el carácter nulo '\0' que indica el final de la cadena
        while (argv[argc - 1][i] != '\0')
            // Imprime el carácter actual de la cadena del último argumento
            write(1, &argv[argc - 1][i++], 1); // Incrementa 'i' después de cada impresión
    }
    // Imprime un salto de línea al final para asegurar que la salida sea legible en la consola
    write(1, "\n", 1);

    return (0); // Retorna 0 para indicar que el programa ha finalizado correctamente
}
