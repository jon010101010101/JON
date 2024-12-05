/*JON BUENA*/

#include <unistd.h>

void rot_13(char *str)
{
    int i = 0;
    char c;

    while (str[i])
    {
        c = str[i];
        if (c >= 'a' && c <= 'z')
        {
            c = ((c - 'a' + 13) % 26) + 'a';
        }
        else if (c >= 'A' && c <= 'Z')
        {
            c = ((c - 'A' + 13) % 26) + 'A';
        }
        write(1, &c, 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        rot_13(argv[1]);
    }
    write(1, "\n", 1);
    return 0;
}

/*SANDRA*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (argv[1][i])
		{
			if ((argv[1][i] >= 'a' && argv[1][i] <= 'm') || (argv[1][i] >= 'A' && argv[1][i] <= 'M'))
				argv[1][i] = argv[1][i] + 13;
			else if ((argv[1][i] >= 'n' && argv[1][i] <= 'z') || (argv[1][i] >= 'N' && argv[1][i] <= 'Z'))
				argv[1][i] = argv[1][i] - 13;
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}




/*IÑAKI*/

#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc == 2)                                              // Si no hay 2 argumentos
    {
        while (argv[1][i] != '\0')                              // Recorro el argumento
        {
            if ((argv[1][i] >= 'A' && argv[1][i] <= 'M')        // Si el carácter esta entre "A" y "M"
                || (argv[1][i] >= 'a' && argv[1][i] <= 'm'))    // o si el carácter esta entre "a" y "m"
                argv[1][i] = argv[1][i] + 13;                   // sumo 13 al codigo ascii
            else if ((argv[1][i] >= 'N' && argv[1][i] <= 'Z')   // Si el carácter esta entre "N" y "Z"
                || (argv[1][i] >= 'n' && argv[1][i] <= 'z'))    // o si el carácter esta entre "n" y "z"
                argv[1][i] = argv[1][i] - 13;                   // resto 13 al codigo ascii
            write(1, &argv[1][i], 1);                           // Escribo el carácter
            i++;                                                // Aumento el contador
        }
    }
    write(1, "\n", 1);                                          // Escribo un salto de linea
    return (0);
}

/*
Assignment name  : rot_13
Expected files   : rot_13.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays it, replacing each of its
letters by the letter 13 spaces ahead in alphabetical order.
'z' becomes 'm' and 'Z' becomes 'M'. Case remains unaffected.
The output will be followed by a newline.
If the number of arguments is not 1, the program displays a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y la muestre, reemplazando cada uno de sus
letras por letra 13 espacios adelante en orden alfabético.
'z' se convierte en 'm' y 'Z' se convierte en 'M'. El caso no se ve afectado.
La salida irá seguida de una nueva línea.
Si el número de argumentos no es 1, el programa muestra una nueva línea.

Example:
$>./rot_13 "abc"
nop
$>./rot_13 "My horse is Amazing." | cat -e
Zl ubefr vf Nznmvat.$
$>./rot_13 "AkjhZ zLKIJz , 23y " | cat -e
NxwuM mYXVWm , 23l $
$>./rot_13 | cat -e
$
$>
$>./rot_13 "" | cat -e
$
$>
*/