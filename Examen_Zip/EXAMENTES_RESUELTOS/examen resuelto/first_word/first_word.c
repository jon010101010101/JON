
/*SANDRA BUENA*/
#include <unistd.h>
int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;
		while (argv[1][i] >= 33 && argv[1][i] <= 126)
		{
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

/*JON BUENA*/

#include <unistd.h>

void print_first_word(char *str)
{
    int i = 0;

    while (str[i] == ' ' || str[i] == '\t')
        i++;
    
    while (str[i] != ' ' && str[i] != '\t' && str[i] != '\0')
    {
        write(1, &str[i], 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        print_first_word(argv[1]);
    }
    write(1, "\n", 1);
    return (0);
}

/*IÑAKI*/
#include <unistd.h>

int ft_type_char(char c)          // Función para controlar que tipo de caracter es
{
    if ((c >= 9 && c <= 13)       // Si "c" es igual a cualquier espacio ascii
                                  //    9  '\t' (horizontal tab
                                  //    10 '\n' (new line)
                                  //    11 '\v' (vertical tab)
                                  //    12 '\f' (form feed)
                                  //    13 '\r' (carriage ret)
        || (c == 32))             // O si "c" es igual 32  ' ' SPACE
        return (0);               // Devuelvo 0
    else if (c >= 33 && c <= 126) // Si "c" es ascii printable ente 33 y 126
         return (1);              // Devuelvo 1
    else
        return (2);               //Devuelvo 2 (OJO 127 NO es printable)
}

int main(int argc, char **argv)
{
    int i;

    i = 0;                                      // Contador para recorrer el argumento
    if (argc == 2)                              // Si hay 2 argumentos
    {
        while ((argv[1][i] != '\0')              // Recorro el argumento mientras el carácter sea de tipo espacio y aumento el contador
            && (ft_type_char(argv[1][i]) == 0))
            i++;
        while ((argv[1][i] != '\0')              // Recorro el argumento mientras el caracter es printable
            && (ft_type_char(argv[1][i]) == 1)) 
            write(1, &argv[1][i++], 1);          // Escribo el carácter y Aumento el contador para recorrer el argumento
    }
    write(1, "\n", 1);                           // Escribo un salto de linea
    return (0);
}



/* Assignment name  : first_word
Expected files   : first_word.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays its first word, followed by a
newline.
A word is a section of string delimited by spaces/tabs or by the start/end of
the string.
If the number of parameters is not 1, or if there are no words, simply display
a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y muestre su primera palabra, seguida 
de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o 
por el inicio/final de la cuerda.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

Examples:
$> ./first_word "FOR PONY" | cat -e
FOR$
$> ./first_word "this        ...       is sparta, then again, maybe    not" | cat -e
this$
$> ./first_word "   " | cat -e
$
$> ./first_word "a" "b" | cat -e
$
$> ./first_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$> */