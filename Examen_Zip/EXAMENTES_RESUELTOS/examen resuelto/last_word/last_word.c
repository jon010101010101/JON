#include <unistd.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')  // Recorro el argumento
        i++;                // Aumento el contador        
    return (i - 1);         // Devuelvo el contador - 1 para obviar el cierre
}

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
    int start;
    int end;
                                                        // Obtengo el tamaño del argumento, 
                                                        // voy al final, 
                                                        // busco el último caracter "end", 
                                                        // recorro hasta el primer caracter 
                                                        // y escribo la palabra desde el primer al último caracter
    start = 0;                                          // Contador para controlar el primer carácter de la última palabra
    end = 0;                                            // Contador para controlar el último carácter de la última palabra
    if (argc == 2)                                      // Si hay 2 argumentos
    {
        start = ft_strlen(argv[1]);                     // Obtengo el tamaño del argumento, sin cierre
        while ((start >= 0)                             // Recorro el argumento mientras no llegue al principio y el carácter sea de tipo espacio y resto 1 al contador 
            && (ft_type_char(argv[1][start]) == 0))
            start--;                                    // Disminuyo el contador
        end = start + 1;                                // Asigno la posición como último carácter
        while ((start >= 0)                             // Recorro el argumento mientras no llegue al principio y el carácter sea de tipo printable y resto 1 al contador 
            && (ft_type_char(argv[1][start]) == 1))
            start--;                                    // Disminuyo el contador
        start++;                                        // Asigno la posición como primer carácter sumando uno ya que en el pao anterior se ha descontado uno de más
        while (start < end)                             // Recorro el argumento mientras no llege al final
        {
            write(1, &argv[1][start], 1);               // Escribo el carácter
            start++;                                    // Aumento del contador
        }
    }
    write(1, "\n", 1);                                  // Escribo un salto de linea
    return (0);
}
/*SANDRA BUENA*/
#include <unistd.h>

void last_word(char *str)
{
	int i = 0;
	int j = 0;
	while (str[i])
	{
		if ((str[i] == ' ' || str[i] == '\t') && (str[i+1] >=33 && str[i+1] <= 126))
			j = i + 1;
		i++;
	}
	while (str[j] >= 33 && str[j] <= 126)
		write(1, &str[j++], 1);
}

int main(int argc, char **argv)
{
 	if (argc == 2)
 	{
 		last_word(argv[1]);
 	}
 	write(1, "\n", 1);
 	return (0);
}



/*
Assignment name  : last_word
Expected files   : last_word.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays its last word followed by a \n.
A word is a section of string delimited by spaces/tabs or by the start/end of
the string.
If the number of parameters is not 1, or there are no words, display a newline.
--------------------------------------------------------------------------------
Escribe un programa que tome una cadena y muestre su última palabra seguida 
de \n.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o 
por el inicio/final de la cadena.
Si el número de parámetros no es 1 o no hay palabras, muestre una nueva línea.

Example:
$> ./last_word "FOR PONY" | cat -e
PONY$
$> ./last_word "this        ...       is sparta, then again, maybe    not" | cat -e
not$
$> ./last_word "   " | cat -e
$
$> ./last_word "a" "b" | cat -e
$
$> ./last_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
$>
*/