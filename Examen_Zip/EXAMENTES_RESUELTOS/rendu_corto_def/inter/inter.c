/*
Assignment name  : inter
Expected files   : inter.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes two strings and displays, without doubles, the
characters that appear in both strings, in the order they appear in the first
one.
The display will be followed by a \n.
If the number of arguments is not 2, the program displays \n.
--------------------------------------------------------------------------------
Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en ambas cadenas, en el orden en que aparecen en la primera
uno.
La pantalla será seguida por un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Examples:
$>./inter "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
padinto$
$>./inter ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6ewg4$
$>./inter "rien" "cette phrase ne cache rien" | cat -e
rien$
$>./inter | cat -e
$
*/

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>

#define SU argv[1][i]
#define SU2 argv[2][j]

int main(int argc, char **argv)
{

    if (argc != 3)
    {
        write(1, "\n", 1);
        return(1);
    }                   
    char seen[256] = {0}; // tamaño max array 255 + 1 incluya cero 
    int i = 0, j;

    while (SU)
	{                            // unsigned char para que sea de 0 a 255   
        if (!seen[(unsigned char)SU]) // verifica que el caracter actual
                                    // no ha sido visto
		{ 
            j = 0;
            while (SU2)
			{
                if (SU == SU2) 
				{ 
                    write(1, &SU, 1);
                    seen[(unsigned char)SU] = 1; //marcado como visto
                    break;
                }
                j++;
            }
        }
        i++;
    }
    write(1, "\n", 1);
    return (0);
}