// Assignment name  : first_word
// Expected files   : first_word.c
// Allowed functions: write
// --------------------------------------------------------------------------------
// Write a program that takes a string and displays its first word, followed by a
// newline.
// A word is a section of string delimited by spaces/tabs or by the start/end of
// the string.
// If the number of parameters is not 1, or if there are no words, simply display
// a newline.
// Examples:
// $> ./first_word "FOR PONY" | cat -e
// FOR$
// $> ./first_word "this        ...       is sparta, then again, maybe    not" | cat -e
// this$
// $> ./first_word "   " | cat -e
// $
// $> ./first_word "a" "b" | cat -e
// $
// $> ./first_word "  lorem,ipsum  " | cat -e
// lorem,ipsum$
// $>
/* SANDRA */

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

/* ANA */

/* #include <unistd.h>

int ft_is_space(char c)
{
	return(c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
	int i;
	int j;

	i = 0;
	j = 0;
	if (argc == 2)
	{
		while (argv[1][i] && ft_is_space(argv[1][i]))
			i++;
		while (argv[1][i])
		{
			if (ft_is_space(argv[1][i]))
				j = 1;
			if (!ft_is_space(argv[1][i]))
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
} */
/* JON CORREGIDA */

/* #include <unistd.h>

void print_first_word(char *str)
{
    int i = 0;
    int first_word_printed = 0;

    while (str[i] == ' ' || str[i] == '\t')
        i++;
    while (str[i] != '\0')
    {
        if (str[i] != ' ' && str[i] != '\t')
        {
            if (first_word_printed)
                write(1, "   ", 3);
            while (str[i] != ' ' && str[i] != '\t' && str[i] != '\0')
            {
                write(1, &str[i], 1);
                i++;
            }
            first_word_printed = 1;
        }
        while (str[i] == ' ' || str[i] == '\t')
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
} */
/* COMENTARIOS CORREGIDA */

/* #include <unistd.h>

// Esta función se encarga de imprimir todas las palabras de la cadena 'str'
// separadas por exactamente tres espacios, eliminando espacios y tabulaciones
// al principio y al final de la cadena.
void print_first_word(char *str)
{
    int i = 0;  // Variable para recorrer la cadena de caracteres.
    int first_word_printed = 0;  // Indicador para saber si ya se ha imprimido la primera palabra.

    // Este bucle se usa para saltar todos los espacios y tabulaciones al principio de la cadena.
    while (str[i] == ' ' || str[i] == '\t')
        i++;

    // Este bucle recorre toda la cadena hasta encontrar el carácter nulo ('\0') que marca el final de 
    la cadena.
    while (str[i] != '\0')
    {
        // Si encontramos un carácter que no es un espacio ni una tabulación, significa que estamos
         en una palabra.
        if (str[i] != ' ' && str[i] != '\t')
        {
            // Si ya se ha imprimido una palabra anteriormente, agregamos tres espacios antes de 
            imprimir la siguiente palabra.
            if (first_word_printed)
                write(1, "   ", 3);  // Escribe tres espacios en la salida estándar (la pantalla).

            // Este bucle se usa para imprimir la palabra carácter por carácter.
            while (str[i] != ' ' && str[i] != '\t' && str[i] != '\0')
            {
                write(1, &str[i], 1);  // Escribe el carácter actual en la salida estándar.
                i++;  // Avanza al siguiente carácter.
            }

            // Después de imprimir la primera palabra, marcamos que ya hemos imprimido una palabra.
            first_word_printed = 1;
        }

        // Este bucle se usa para saltar los espacios y tabulaciones entre las palabras.
        while (str[i] == ' ' || str[i] == '\t')
            i++;
    }
}

int main(int argc, char **argv)
{
    // Verifica si se ha pasado exactamente un argumento al programa (además del nombre del programa).
    if (argc == 2)
    {
        // Si se pasa un argumento, llama a la función print_first_word para procesar la cadena.
        print_first_word(argv[1]);
    }

    // Independientemente de si se ha pasado un argumento válido o no, imprime una nueva línea.
    write(1, "\n", 1);

    // Termina la ejecución del programa devolviendo 0, lo que indica que el programa se ejecutó correctamente.
    return (0);
} */









/* NO DA BIEN

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
} */

/* COMENTARIOS */

/* #include <unistd.h>  // Incluimos la biblioteca unistd.h para usar la función write

// Definimos la función print_first_word, que toma como argumento un puntero a una cadena de caracteres (str)
void print_first_word(char *str)
{
    int i = 0;  // Declaramos la variable i, que será utilizada como índice para recorrer la cadena

    // Este bucle avanza en la cadena mientras el carácter actual sea un espacio (' ') o una tabulación ('\t')
    // El objetivo es saltarse cualquier espacio o tabulación al principio de la cadena
    while (str[i] == ' ' || str[i] == '\t')
        i++;
    
    // Este bucle imprime la primera palabra de la cadena.
    // Continúa imprimiendo caracteres mientras no se encuentre un espacio, tabulación o el final de la cadena ('\0')
    while (str[i] != ' ' && str[i] != '\t' && str[i] != '\0')
    {
        write(1, &str[i], 1);  // Escribe el carácter actual en la salida estándar
        i++;  // Avanza al siguiente carácter en la cadena
    }
}

// La función principal main, que recibe el número de argumentos (argc) y un array de strings (argv)
int main(int argc, char **argv)
{
    // Verificamos si hay exactamente dos argumentos (el nombre del programa y un argumento adicional)
    if (argc == 2)
    {
        // Llamamos a la función print_first_word, pasando el segundo argumento (argv[1]) que es la cadena a procesar
        print_first_word(argv[1]);
    }
    // Imprimimos un salto de línea después de imprimir la primera palabra
    write(1, "\n", 1);
    
    return (0);  // Devolvemos 0 para indicar que el programa terminó correctamente
} */