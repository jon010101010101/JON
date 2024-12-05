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

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        char SU;

        SU = argv[1][i];
        // Saltar espacios y tabulaciones iniciales
        while (SU == ' ' || SU == '\t')
        
            i++;
        

        // Imprimir caracteres dentro del rango ASCII imprimible
        while (SU >= 33 && SU <= 126)
        {
             // Asignar el carácter actual a SU
            write(1, &SU, 1); // Imprimir el carácter usando SU
            i++;
        }
    }
    write(1, "\n", 1); // Imprimir un salto de línea al final
    return (0);
}




/* SANDRA */

/* #include <unistd.h>
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
} */
/* COMENTARIOS */

/* #include <unistd.h>  // Se incluye la librería unistd.h que proporciona la función write

int main(int argc, char **argv)  // Función principal que recibe el número de argumentos (argc) y los argumentos en sí (argv)
{
    // Verificamos si el número de argumentos es igual a 2
    if (argc == 2)
    {
        int i = 0;  // Declaramos e inicializamos la variable i para usarla como índice en el bucle

        // Este bucle avanza en la cadena mientras encuentre espacios o tabulaciones
        while (argv[1][i] == ' ' || argv[1][i] == '\t')
            i++;  // Incrementa el índice para saltar espacios y tabulaciones al principio de la cadena

        // Este bucle imprime caracteres desde la posición actual del índice mientras sean visibles (es decir, entre '!' y '~' en la tabla ASCII)
        while (argv[1][i] >= 33 && argv[1][i] <= 126)
        {
            write(1, &argv[1][i], 1);  // Escribe el carácter actual en la salida estándar
            i++;  // Avanza al siguiente carácter
        }
    }

    write(1, "\n", 1);  // Escribe un salto de línea en la salida estándar

    return (0);  // Retorna 0, indicando que el programa finalizó correctamente
} */

