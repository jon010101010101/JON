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
    int j;
    int k;

    i = 0;                                              // Contador para recorrer el argumento
    j = 0;                                              // Contador para controlar el inicio de palabra
    k = 0;                                              // Contador para obviar espacios iniciales
    if (argc == 2)                                      // Si hay 2 argumentos
    {
        while ((argv[1][i] != '\0')                     // Recorro el argumento mientras el carácter sea de tipo espacio y aumento el contador
            && (ft_type_char(argv[1][i]) == 0))
            i++;
        while (argv[1][i] != '\0')                      // Recorro el argumento
        {
            if ((ft_type_char(argv[1][i]) == 1)         // Si el caracter es printable
                && (ft_type_char(argv[1][i - 1]) == 0)  // y el anterior es un espacio
                && k == 1)                              // y no de los del principio (es decir ya ha habido alguna palabra)
                j = 1;                                  // Contador para controlar espacios a 1
            if (ft_type_char(argv[1][i]) == 1)          // Si el caracter es printable
            {
                k = 1;                                  // Contador para obviar espacios iniciales a 1
                if (j == 1)                             // Si el contador para controlar espacios es 1
                {
                    write(1, "   ", 3);                 // Escribo 3 espacios
                    j = 0;                              // Contador para controlar espacios a 0
                }
                write(1, &argv[1][i], 1);               // Escribo el carácter
            }
            i++;                                        // Aumento el contador para recorrer el argumento
        }
    }
    write(1, "\n", 1);                                  // Escribo un salto de linea
    return (0);
}

/*SANDRA BUENA*/
#include <unistd.h>

int	main(int argc, char **argv)
{
	int i = 0;
	int j = 0;
	if (argc == 2)
	{
		while (argv[1][i] == ' ' || argv[1][i] == '\t')
			i++;
		while (argv[1][i])
		{
			if (argv[1][i] == ' ' || argv[1][i] == '\t')
				j = 1;
			if (!(argv[1][i] == ' ' || argv[1][i] == '\t'))
			{
				if (j)
					write(1, "   ", 3);
				j = 0;
				write(1, &argv[1][i], 1);
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}



/*
Escribe un programa que tome una cadena y la muestre exactamente con tres espacios.
entre cada palabra, sin espacios ni tabulaciones ni al principio ni al final,
seguido de una nueva línea.
Una palabra es una sección de cadena delimitada por espacios/tabulaciones o por el
inicio/final de la cadena.
Si el número de parámetros no es 1, o si no hay palabras, simplemente muestre
una nueva línea.

Examples:
$> ./expand_str "vous   voyez   c'est   facile   d'afficher   la   meme   chose" | cat -e
vous   voyez   c'est   facile   d'afficher   la   meme   chose$
$> ./expand_str " seulement          la c'est      plus dur " | cat -e
seulement   la   c'est   plus   dur$
$> ./expand_str "comme c'est cocasse" "vous avez entendu, Mathilde ?" | cat -e
$
$> ./expand_str "" | cat -e */