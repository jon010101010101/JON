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

/* SANDRA OK*/

/* #include <unistd.h>

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
} */

/* #include <unistd.h>

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        write(1, "\n", 1);
        return 0;
    }

    char *str = argv[1];
    char ch;

    while ((ch = *str))
    {
        if (ch >= 'a' && ch <= 'z')
        {
            // Mueve 'a' a 'y' a la siguiente letra
            if (ch == 'z') 
                ch = 'a';
            else 
                ch++;
        }
        else if (ch >= 'A' && ch <= 'Z')
        {
            // Mueve 'A' a 'Y' a la siguiente letra
            if (ch == 'Z')
                ch = 'A';
            else
                ch++;
        }
        write(1, &ch, 1); // Imprime el carácter modificado
        str++;
    }
    write(1, "\n", 1); // Imprime un salto de línea al final
    return (0);
} */

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        char SU;

        while (argv[1][i] != '\0')
        {
            SU = argv[1][i]; // Asignamos el carácter actual a SU
            if ((SU >= 'a' && SU < 'z') || (SU >= 'A' && SU < 'Z'))
                SU = SU + 1; // Incrementa el carácter
            else if (SU == 'z')
                SU = 'a'; // Caso especial para 'z'
            else if (SU == 'Z')
                SU = 'A'; // Caso especial para 'Z'
            write(1, &SU, 1); // Imprime el carácter modificado
            i++;
        }
    }
    write(1, "\n", 1); // Imprime un salto de línea al final
    return 0;
}
