/*SANDRA*/

#include <unistd.h>

int not_seen_before(char *str, char c, int max_pos)
{
    int i = 0;
    while (i < max_pos)
    {
        if (str[i] == c)
            return (0);
        i++;
    }
    return (1);
}

void ft_union(char *s1, char *s2)
{
    int i = 0;
    int j = 0;

    while (s1[i])
    {
        if (not_seen_before(s1, s1[i], i))
            write(1, &s1[i], 1);
        i++;
    }
    while (s2[j])
    {
        if (not_seen_before(s1, s2[j], i) && not_seen_before(s2, s2[j], j))
            write(1, &s2[j], 1);
        j++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 3)
        ft_union(argv[1], argv[2]);
    write(1, "\n", 1);
    return (0);
}


/*JON BUENO*/

#include <unistd.h>

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

int     check_seen(char *str, char c, int pos)
{
    int i = 0;
    while (i < pos)
    {
        if (str[i] == c)
            return (1);
        i++;
    }
    return (0);
}

void    union_strings(char *s1, char *s2)
{
    int i = 0;
    int j = 0;
    
    while (s1[i])
    {
        if (!check_seen(s1, s1[i], i))
            ft_putchar(s1[i]);
        i++;
    }
    while (s2[j])
    {
        if (!check_seen(s1, s2[j], i) && !check_seen(s2, s2[j], j))
            ft_putchar(s2[j]);
        j++;
    }
    ft_putchar('\n');
}

int     main(int argc, char **argv)
{
    if (argc != 3)
    {
        ft_putchar('\n');
        return (1);
    }
    union_strings(argv[1], argv[2]);
    return (0);
}

/*JON BUENA*/

#include <unistd.h>

int has_been_printed(char c, char *printed, int length)
{
    int i = 0;
    while (i < length)
    {
        if (printed[i] == c)
            return 1;
        i++;
    }
    return 0;
}

void union_strings(char *str1, char *str2)
{
    char printed[256] = {0};
    int length = 0;
    int i = 0;

        while (str1[i] != '\0')
    {
        if (!has_been_printed(str1[i], printed, length))
        {
            write(1, &str1[i], 1);
            printed[length++] = str1[i];
        }
        i++;
    }

    i = 0;
    while (str2[i] != '\0')
    {
        if (!has_been_printed(str2[i], printed, length))
        {
            write(1, &str2[i], 1);
            printed[length++] = str2[i];
        }
        i++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 3)
    {
        union_strings(argv[1], argv[2]);
    }
    write(1, "\n", 1);
    return (0);
}

/*IÑAKI*/

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
            if (ft_single_in_param(argv[1], argv[1][i], i) == 0)    // Si el carácter no esta duplicado en el argumento 1
                write(1, &argv[1][i], 1);                           // Escribo el carácter
            i++;                                                    // Aumento el contador
        }   
        i = 0;                                                      // IMPORTANTE Reinicio el contador a 0 para recorrer el argumento 2
        while (argv[2][i] != '\0')                                  // Recorro el argumento 2
        {
            if ((ft_single_in_param(argv[2], argv[2][i], i) == 0)   // Si el carácter no esta duplicado en el argumento 2
                && (ft_in_other_param(argv[1], argv[2][i]) == 0))   // y el caracter no existe en el argumento 1
                write(1, &argv[2][i], 1);                           // Escribo el carácter
            i++;                                                    // Aumento el contador
        }                 
    }
    write(1, "\n", 1);                                              // Escribo un salto de linea
    return (0);
}


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