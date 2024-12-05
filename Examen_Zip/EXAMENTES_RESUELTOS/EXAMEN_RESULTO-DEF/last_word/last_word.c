/*Assignment name  : last_word
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
$>*/
/*  */

/* #include <unistd.h>

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
} */

/* COMENTARIOS */

/* #include <unistd.h>  // Se incluye la librería unistd.h para poder usar la función write

// Función que encuentra e imprime la última palabra de la cadena de caracteres pasada como argumento
void last_word(char *str)
{
    int i = 0;  // Declaramos e inicializamos la variable i para usarla como índice en la cadena
    int j = 0;  // Declaramos e inicializamos la variable j, que usaremos para marcar el inicio de la última palabra

    // Bucle que recorre la cadena de caracteres hasta el final
    while (str[i])
    {
        // Si el carácter actual es un espacio o tabulación, y el siguiente carácter es un carácter visible,
        // entonces marcamos j como el inicio de la próxima palabra
        if ((str[i] == ' ' || str[i] == '\t') && (str[i+1] >= 33 && str[i+1] <= 126))
            j = i + 1;  // Actualizamos j para que apunte al inicio de la última palabra encontrada
        i++;  // Avanzamos al siguiente carácter de la cadena
    }

    // Bucle que imprime la última palabra encontrada en la cadena
    while (str[j] >= 33 && str[j] <= 126)
        write(1, &str[j++], 1);  // Escribimos el carácter actual en la salida estándar y avanzamos al siguiente
}

int main(int argc, char **argv)  // Función principal que recibe el número de argumentos y los argumentos en sí
{
    // Si el número de argumentos es exactamente 2, ejecuta la función last_word con el argumento proporcionado
    if (argc == 2)
    {
        last_word(argv[1]);  // Llamada a la función last_word con la cadena pasada como segundo argumento
    }

    write(1, "\n", 1);  // Escribe un salto de línea en la salida estándar

    return (0);  // Retorna 0 indicando que el programa finalizó correctamente
} */

#include <unistd.h>

int ft_is_space(char c) {
    return (c == 32 || c == 9);
}
int main(int argc, char **argv)
{
    int i;
    int start;
    char SU;
    char SU_next;
    char SU_START;

    i = 0;
    start = 0;
    if (argc == 2)
	{
        while (argv[1][i])
		{
            SU = argv[1][i]; // Asigna el carácter actual a SU
            SU_next = argv[1][i + 1]; // Asigna el siguiente carácter a SU_next
            if (SU_next >= 33 && SU_next <= 126 && ft_is_space(SU))
			{
                start = i + 1;
            }
            i++;
        }
        // Asigna el carácter al inicio del segmento imprimible a SU_START
        SU_START = argv[1][start];
        while (SU_START >= 33 && SU_START <= 126)
		{
            write(1, &SU_START, 1);
            start++;
            SU_START = argv[1][start]; // Actualiza SU_START al siguiente carácter
        }
    }
    write(1, "\n", 1);
    return 0;
}



/* ANA */
/* #include <unistd.h>

int ft_is_space(char c)
{
	return(c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
	int i;
	int start;

	i = 0;
	start = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (argv[1][i + 1] >= 33 && argv[1][i + 1] <= 126 && ft_is_space(argv[1][i]))
				start = i + 1;
			i++;
		}
		while (argv[1][start] >= 33 && argv[1][start] <= 126)
		{
			write(1, &argv[1][start], 1);
			start++;
		}
	}
	write(1, "\n", 1);
	return (0);

} */


