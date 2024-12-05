#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc > 1)                       // Si hay más de 1 argumento
    {
        while (argv[1][i] != '\0')      // Recorro el argumento
            write(1, &argv[1][i++], 1); // Escribo el carácter y aumento el contador
    }
    write(1, "\n", 1);                  // Escribo un salto de linea
    return (0);
}


/*Assignment name  : aff_first_param
Expected files   : aff_first_param.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes strings as arguments, and displays its first
argument followed by a \n.
If the number of arguments is less than 1, the program displays \n.
-------------------------------------------------- ------------------------------
Escribe un programa que tome cadenas como argumentos y muestre su primer
argumento seguido de un \n.
Si el número de argumentos es menor que 1, el programa muestra \n.

Example:
$> ./aff_first_param vincent mit "l'ane" dans un pre et "s'en" vint | cat -e
vincent$
$> ./aff_first_param "j'aime le fromage de chevre" | cat -e
j'aime le fromage de chevre$
$> ./aff_first_param | cat -e
$*/