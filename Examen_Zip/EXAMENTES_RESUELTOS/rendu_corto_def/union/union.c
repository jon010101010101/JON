/*
Assignment name  : union
Expected files   : union.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in either one of the strings.
The display will be in the order characters appear in the command line, and
will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en cualquiera de las cadenas.
La pantalla se mostrará en el orden en que aparecen los caracteres en la línea 
de comando y irá seguido de un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Example:
$>./union zpadinton "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
zpadintoqefwjy$
$>./union ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6vewg4thras$
$>./union "rien" "cette phrase ne cache rien" | cat -e
rienct phas$
$>./union | cat -e
$
$>
$>./union "rien" | cat -e
$
$>
*/

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>

#define SU argv[1][i]
#define SU2 argv[2][j]

int main(int argc, char **argv)
{
    if(argc != 3)
    {
        write(1, "\n", 1);
        return(1);
    }
        
    char seen[256] = {0};
    int i = 0;
    int j = 0;

    while(SU)
    {
        if (!seen[(unsigned char)SU])
        {
            seen[(unsigned char)SU] = 1;
            write(1, &SU, 1);
        }
        i++;
    }
    while(SU2)
    {
        if (!seen[(unsigned char)SU2])
        {
            seen[(unsigned char)SU2] = 1;
            write(1, &SU2, 1);
        }
        j++;
    }
    write(1, "\n", 1);
    return (0);
}