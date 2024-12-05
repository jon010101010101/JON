#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc > 1)                               // Si hay más de 1 argumento
    {
        while (argv[argc - 1][i] != '\0')       // Recorro el último argumento
            write(1, &argv[argc - 1][i++], 1);  // Escribo el carácter y aumento el contador
    }
    write(1, "\n", 1);                          // Escribo un salto de linea
    return (0);
}

/* Assignment name  : aff_last_param
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
$ */