/*
Assignment name  : rotone
Expected files   : rotone.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays it, replacing each of its
letters by the next one in alphabetical order.
'z' becomes 'a' and 'Z' becomes 'A'. Case remains unaffected.
The output will be followed by a \n.
If the number of arguments is not 1, the program displays \n.
-------------------------------------------------- ------------------------------
Escribe un programa que tome una cadena y la muestre, reemplazando cada uno de sus
letras por la siguiente en orden alfabético.
'z' se convierte en 'a' y 'Z' se convierte en 'A'. El caso no se ve afectado.
La salida irá seguida de un \n.
Si el número de argumentos no es 1, el programa muestra \n.

Example:
$>./rotone "abc"
bcd
$>./rotone "Les stagiaires du staff ne sentent pas toujours tres bon." | cat -e
Mft tubhjbjsft ev tubgg of tfoufou qbt upvkpvst usft cpo.$
$>./rotone "AkjhZ zLKIJz , 23y " | cat -e
BlkiA aMLJKa , 23z $
$>./rotone | cat -e
$
$>
$>./rotone "" | cat -e
$
$>
*/
/* OK MAQUINA */
#include <unistd.h>  // Incluye la biblioteca estándar para usar la función write

#define SU argv[1][i]  // Define un alias 'SU' para acceder al carácter actual en el primer argumento

int main(int argc, char **argv)
{
    // Verifica si se ha proporcionado exactamente un argumento adicional
    if (argc == 2)
    {
        int i = 0;  // Índice para recorrer la cadena del primer argumento

        // Recorre cada carácter del primer argumento hasta llegar al final
        while (SU)
        {
            // Verifica si el carácter actual es una letra minúscula (excepto 'z') o una letra mayúscula (excepto 'Z')
            if ((SU >= 'a' && SU < 'z') || (SU >= 'A' && SU < 'Z'))
                SU = SU + 1;  // Incrementa el carácter para obtener la siguiente letra en el alfabeto
            // Verifica si el carácter actual es 'z'
            else if (SU == 'z')
                SU = 'a';  // Cambia 'z' a 'a' para hacer un "wrap-around" en el alfabeto
            // Verifica si el carácter actual es 'Z'
            else if (SU == 'Z')
                SU = 'A';  // Cambia 'Z' a 'A' para hacer un "wrap-around" en el alfabeto
            write(1, &SU, 1);  // Imprime el carácter modificado
            i++;  // Avanza al siguiente carácter en la cadena
        }
    }

    // Imprime una nueva línea después de que todos los caracteres hayan sido procesados para asegurar una salida limpia
    write(1, "\n", 1);
    return 0;  // Termina el programa exitosamente
}

