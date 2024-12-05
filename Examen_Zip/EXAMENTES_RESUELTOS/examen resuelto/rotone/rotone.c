/*SANDRA*/
#include <unistd.h>

int main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (argv[1][i] != '\0')
		{
			if ((argv[1][i] >= 'a' && argv[1][i] < 'z') || (argv[1][i] >= 'A' && argv[1][i] < 'Z'))
				argv[1][i] = argv[1][i] + 1;
			else if (argv[1][i] == 'z')
				argv[1][i] = 'a';
			else if (argv[1][i] == 'Z')
				argv[1][i] = 'A';
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}


/*JON BUENA*/

#include <unistd.h>

void rotone(char *str)
{
    int i = 0;
    char c;

    while (str[i])
    {
        c = str[i];
        if (c >= 'a' && c <= 'z')
        {
            if (c == 'z')
                c = 'a';
            else
                c = c + 1;
        }
        else if (c >= 'A' && c <= 'Z')
        {
            if (c == 'Z')
                c = 'A';
            else
                c = c + 1;
        }
        write(1, &c, 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        rotone(argv[1]);
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
            if ((argv[1][i] >= 'A' && argv[1][i] < 'Z')         // Si el carácter esta entre "A" e "Y"
                || (argv[1][i] >= 'a' && argv[1][i] < 'z'))     // o si el carácter esta entre "a" e "y"
                argv[1][i] = argv[1][i] + 1;                    // sumo 1 al codigo ascii
            else if (argv[1][i] == 'Z')                         // Si el carácter es "Z"
                argv[1][i] = 'A';                               // Le asigno "A"
            else if (argv[1][i] == 'z')                         // Si el carácter es "Z"
                argv[1][i] = 'a';                               // Le asigno "A"
            write(1, &argv[1][i], 1);                           // Escribo el carácter
            i++;                                                // Aumento el contador
        }
    }
    write(1, "\n", 1);                                          // Escribo siempre un salto de linea
    return (0);
}

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