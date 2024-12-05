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



/* ANA OK*/

/* #include <unistd.h>

int	ft_is_space(char c)
{
	return (c == ' ' || c == '\t');
}

int	main(int argc, char **argv)
{
	int	i;
	int	start;

	i = 0;
	start = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (ft_is_space(argv[1][i]) && (argv[1][i + 1] >= 33 && argv[1][i + 1] <= 126))
				start = i + 1;
			i++;
 		}
		while (argv[1][start] >= 33 && argv[1][start] <= 126)
		{	
			write(1, &argv[1][start], 1);
			start ++;
		}
	}
		write(1, "\n", 1);
		return(0);
} */
/* COMENTARIOS ANA */

/* #include <unistd.h>

// Función que determina si un carácter es un espacio en blanco o tabulación
int ft_is_space(char c)
{
    // Retorna 1 (verdadero) si el carácter es un espacio o tabulación, 0 (falso) en caso contrario
    return (c == ' ' || c == '\t');
}

int main(int argc, char **argv)
{
    // Declaración de variables
    int i;      // Índice para recorrer la cadena de caracteres
    int start;  // Índice que marcará el inicio de la última palabra encontrada

    i = 0;
    start = 0;

    // Verifica si se ha pasado un solo argumento (además del nombre del programa)
    if (argc == 2)
    {
        // Recorre la cadena de caracteres hasta encontrar el final
        while (argv[1][i])
        {
            // Verifica si el carácter actual es un espacio o tabulación,
            // y si el siguiente carácter es un carácter imprimible (parte de una palabra)
            if (ft_is_space(argv[1][i]) && (argv[1][i + 1] >= 33 && argv[1][i + 1] <= 126))
                start = i + 1;  // Actualiza 'start' para marcar el inicio de una nueva palabra
            i++;  // Incrementa el índice para seguir recorriendo la cadena
        }

        // Imprime la última palabra encontrada carácter por carácter
        while (argv[1][start] >= 33 && argv[1][start] <= 126)
        {   
            write(1, &argv[1][start], 1);  // Escribe el carácter en la salida estándar
            start++;  // Avanza al siguiente carácter de la palabra
        }
    }

    // Imprime un salto de línea al final
    write(1, "\n", 1);
    return (0);  // Retorna 0 indicando que el programa terminó exitosamente
} */


/* ES CORRECCTO PERO MEJOR LA OTRA QUE SE PARECE A FIRST WORD */
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

/* #include <unistd.h>  // Incluimos la biblioteca unistd.h para usar la función write

// Función que encuentra y escribe la última palabra de una cadena
void last_word(char *str)
{
    int i = 0;  // Inicializamos un índice i en 0 para recorrer la cadena
    int j = 0;  // Inicializamos un índice j en 0 que marcará el inicio de la última palabra

    // Bucle para recorrer la cadena de caracteres
    while (str[i])
    {
        // Si encontramos un espacio (' ') o tabulación ('\t') seguido de un carácter imprimible
        // (es decir, un carácter que no sea un espacio o un símbolo de control)
        if ((str[i] == ' ' || str[i] == '\t') && (str[i + 1] >= 33 && str[i + 1] <= 126))
            j = i + 1;  // Actualizamos j para que apunte al inicio de la próxima palabra
        i++;  // Incrementamos i para seguir recorriendo la cadena
    }

    // Bucle para escribir la última palabra encontrada
    while (str[j] >= 33 && str[j] <= 126)
        write(1, &str[j++], 1);  // Escribimos carácter por carácter la última palabra
}

// Función principal del programa
int main(int argc, char **argv)
{
    // Verificamos que el programa haya recibido exactamente un argumento
    if (argc == 2)
    {
        last_word(argv[1]);  // Llamamos a la función last_word con el argumento recibido
    }
    write(1, "\n", 1);  // Escribimos un salto de línea al final de la salida
    return (0);  // Retornamos 0 para indicar que el programa terminó con éxito
} */

