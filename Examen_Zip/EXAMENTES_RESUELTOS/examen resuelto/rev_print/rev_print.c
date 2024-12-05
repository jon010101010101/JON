/*JON BUENA*/
#include <unistd.h>
#include <string.h>

void print_reversed(const char *str)
{
    if (*str != '\0')
    {
        print_reversed(str + 1);
        write(1, str, 1);
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        print_reversed(argv[1]);
    }
    write(1, "\n", 1);
    return (0);
}


#include <unistd.h>
#include <string.h>

// Función recursiva para imprimir los caracteres de la cadena en orden inverso
void print_reversed(const char *str)
{
    // Caso base: si el carácter actual es el terminador nulo, termina la recursión
    if (*str != '\0')
    {
        // Llamada recursiva con la siguiente dirección de memoria en la cadena
        print_reversed(str + 1);

        // Imprime el carácter actual después de que se hayan impreso los caracteres siguientes
        write(1, str, 1);
    }
}

int main(int argc, char **argv)
{
    // Verifica si el número de argumentos es exactamente 2
    if (argc == 2)
    {
        // Llama a la función para imprimir la cadena al revés
        print_reversed(argv[1]);
    }
    // Imprime una nueva línea en todos los casos
    write(1, "\n", 1);

    return (0);
}






/*JON FUNCIONA BIEN*/

#include <unistd.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
        i++;
    return (i);
}

int main(int argc, char **argv)
{
    int i;

    if (argc == 2)
    {
        i = ft_strlen(argv[1]) - 1;
        while (i >= 0)
        {
            write(1, &argv[1][i], 1);
            i--;
        }
    }
    write(1, "\n", 1);
    return (0);
}

/*IÑAKI*/

#include <unistd.h>
#include <stdio.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')  // Recorro el argumento
        i++;                // Aumento el contador        
    return (i - 1);         // Devuelvo el contador - 1 para obviar el cierre
}

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc == 2)                      // Si hay 2 argumentos
    {
        i = ft_strlen(argv[1]);         // Obtengo el tamaño del argumento, sin cierre
        while (argv[1][i] != '\0')      // Recorro el argumento en orden inverso
        {
            write(1, &argv[1][i], 1);   // Escribo el carácter
            i--;                        // Retrocedo el contador
        }
    }
    write(1, "\n", 1);                  // Escribo siempre un salto de linea
    return (0);
}

/*SANDRA ESTA BIEN*/
#include <unistd.h>
int str_len(char *str)
{
	int n = 0;
	while (str[n])
		n++;
	return (n);
}

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int len = str_len(argv[1]) - 1;
		while (len >= 0)
		{
			write(1, &argv[1][len--], 1);
		}
	}
	write(1, "\n", 1);
	return (0);
}

/*
Assignment name  : rev_print
Expected files   : rev_print.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string, and displays the string in reverse
followed by a newline.
If the number of parameters is not 1, the program displays a newline.
-------------------------------------------------- ------------------------------
Escribe un programa que tome una cadena y la muestre al revés
seguido de una nueva línea.
Si el número de parámetros no es 1, el programa muestra una nueva línea.

Examples:
$> ./rev_print "zaz" | cat -e
zaz$
$> ./rev_print "dub0 a POIL" | cat -e
LIOP a 0bud$
$> ./rev_print | cat -e
$
*/