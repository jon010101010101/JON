/*SANDRA*/
#include <unistd.h>

int	inter(char *str, char c, int max_pos)
{
	int i = 0;
	while (str[i] && (i < max_pos || max_pos == -1))
		if (str[i++] == c)
			return (1);
	return (0);
}

int	main(int argc, char **argv)
{
	if (argc == 3)
	{
		int i = 0;
		while (argv[1][i])
		{
			if (!inter(argv[1], argv[1][i], i) && inter(argv[2], argv[1][i], -1))
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

/*OTRA JON BUENA*/
#include <unistd.h>

void inter(char *first, char *second)
{
    int i = 0, j;
    int found;

    while (first[i] != '\0')
    {
        found = 0;
        j = 0;
        while (j < i)
        {
            if (first[j] == first[i])
            {
                found = 1;
                break;
            }
            j++;
        }
        if (!found)
        {
            j = 0;
            while (second[j] != '\0')
            {
                if (second[j] == first[i])
                {
                    write(1, &first[i], 1);
                    break;
                }
                j++;
            }
        }
        i++;
    }
    write(1, "\n", 1);
}

int main(int argc, char **argv)
{
    if (argc != 3)
    {
        write(1, "\n", 1);
        return (0);
    }

    inter(argv[1], argv[2]);
    return (0);
}

/*JON BUENA*/

#include <unistd.h>

int is_in_string(char c, char *str)
{
    while (*str)
    {
        if (*str == c)
            return 1;
        str++;
    }
    return 0;
}

int has_been_printed(char c, char *printed, int length)
{
    for (int i = 0; i < length; i++)
    {
        if (printed[i] == c)
            return 1;
    }
    return 0;
}

void inter(char *str1, char *str2)
{
    char printed[256] = {0};
    int length = 0;

    for (int i = 0; str1[i] != '\0'; i++)
    {
        if (is_in_string(str1[i], str2) && !has_been_printed(str1[i], printed, length))
        {
            write(1, &str1[i], 1);
            printed[length++] = str1[i];
        }
    }
}

int main(int argc, char **argv)
{
    if (argc == 3)
    {
        inter(argv[1], argv[2]);
    }
    write(1, "\n", 1);
    return 0;
}



#include <unistd.h>

int ft_single_in_param(char *str, char c, int i)
{
    int j;
                                        // "str" es el parametro en el que buscar
                                        // "c" es el carácter a buscar
                                        // "i" es la posición en la que se encuentra el carácter en "str"
    j = 0;                              // Contador para recorrer str
    while (str[j] != '\0' && j < i)     // Recorro el argumento mientras no haya llegado a la posición del carácter a buscar
    {
        if (str[j] == c)                // Si coinciden es que en una posición anterior ya existe "c"
            return (1);             
        j++;                            // Aumento el contador 
    }
    return (0);
}

int ft_in_other_param(char *str, char c)
{
    int i;
                            // "str" es el parametro en el que buscar
                            // "c" es el carácter a buscar

    i = 0;                  // Contador para recorrer str
    while (str[i] != '\0')  // Recorro el argumento mientras no haya llegado a la posición del carácter a buscar
    {
        if (str[i] == c)    // Si coinciden es que en una posición del otro argumento ya existe "c"
            return (1);
        i++;                // Aumento el contador
    }
    return (0);
}

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc == 3)                                                  // Si hay 3 argumentos
    {
        while (argv[1][i] != '\0')                                  // Recorro el argumento 1
        {
            if ((ft_single_in_param(argv[1], argv[1][i], i) == 0)   // Si el carácter no esta duplicado en el argumento 1
                && (ft_in_other_param(argv[2], argv[1][i]) == 1))   // y el caracter existe en el argumento 2
                write(1, &argv[1][i], 1);                           // Escribo el carácter
            i++;                                                    // Aumento el contador
        }           
    }
    write(1, "\n", 1);                                              // Escribo siempre un salto de linea
    return (0);
}



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