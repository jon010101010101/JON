/*Escribe un programa que tome una cadena y la muestre, reemplazando cada uno de sus
letras por letra 13 espacios adelante en orden alfabético.
'z' se convierte en 'm' y 'Z' se convierte en 'M'. El caso no se ve afectado.
La salida irá seguida de una nueva línea.
Si el número de argumentos no es 1, el programa muestra una nueva línea.

Example:
$>./rot_13 "abc"
nop
$>./rot_13 "My horse is Amazing." | cat -e
Zl ubefr vf Nznmvat.$
$>./rot_13 "AkjhZ zLKIJz , 23y " | cat -e
NxwuM mYXVWm , 23l $
$>./rot_13 | cat -e
$
$>
$>./rot_13 "" | cat -e
$
$>*/

/* SANDRA OK*/

#include <unistd.h>

int	main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (argv[1][i])
		{
			if ((argv[1][i] >= 'a' && argv[1][i] <= 'm') || (argv[1][i] >= 'A' && argv[1][i] <= 'M'))
				argv[1][i] = argv[1][i] + 13;
			else if ((argv[1][i] >= 'n' && argv[1][i] <= 'z') || (argv[1][i] >= 'N' && argv[1][i] <= 'Z'))
				argv[1][i] = argv[1][i] - 13;
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

/* ANA */

/* #include <unistd.h>

int main(int argc, char **argv)
{
	int	i;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if (((argv[1][i] >= 'a') && (argv[1][i] <= 'm')) || ((argv[1][i] >= 'A') && (argv[1][i] <= 'M')))
				argv[1][i] = argv[1][i] + 13;
			if (((argv[1][i] > 'm') && (argv[1][i] <= 'z')) || ((argv[1][i] > 'M') && (argv[1][i] <= 'Z')))
				argv[1][i] = argv[1][i] - 13;	
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return(0);
} */
/* COMENTARIOS ANA */

/* #include <unistd.h>   // Incluimos la biblioteca unistd.h para usar la función write

int main(int argc, char **argv)
{
	int	i;  // Declaramos una variable entera i que servirá como índice para recorrer la cadena

	i = 0;  // Inicializamos i en 0 para empezar a recorrer la cadena desde el primer carácter

	// Verificamos que el programa haya recibido exactamente un argumento adicional
	if (argc == 2)
	{
		// Recorremos la cadena carácter por carácter hasta llegar al final ('\0')
		while (argv[1][i])
		{
			// Verificamos si el carácter es una letra entre 'a' y 'm' o entre 'A' y 'M'
			// Estas letras serán desplazadas 13 posiciones hacia adelante
			if (((argv[1][i] >= 'a') && (argv[1][i] <= 'm')) || ((argv[1][i] >= 'A') && (argv[1][i] <= 'M')))
				argv[1][i] = argv[1][i] + 13;

			// Verificamos si el carácter es una letra entre 'n' y 'z' o entre 'N' y 'Z'
			// Estas letras serán desplazadas 13 posiciones hacia atrás
			if (((argv[1][i] > 'm') && (argv[1][i] <= 'z')) || ((argv[1][i] > 'M') && (argv[1][i] <= 'Z')))
				argv[1][i] = argv[1][i] - 13;	

			// Escribimos el carácter modificado en la salida estándar
			write(1, &argv[1][i], 1);

			// Incrementamos el índice i para pasar al siguiente carácter
			i++;
		}
	}

	// Escribimos un salto de línea en la salida estándar
	write(1, "\n", 1);

	// Retornamos 0 para indicar que el programa terminó con éxito
	return(0);
} */

/* #include <unistd.h>

void rot_13(char *str)
{
    int i = 0;
    char c;

    while (str[i])
    {
        c = str[i];
        if (c >= 'a' && c <= 'z')
        {
            c = ((c - 'a' + 13) % 26) + 'a';
        }
        else if (c >= 'A' && c <= 'Z')
        {
            c = ((c - 'A' + 13) % 26) + 'A';
        }
        write(1, &c, 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        rot_13(argv[1]);
    }
    write(1, "\n", 1);
    return 0;
} */


/* COMENTARIOS */

/* #include <unistd.h>

// Función que aplica el cifrado ROT13 a una cadena de caracteres.
void rot_13(char *str)
{
    int i = 0;      // Inicializa el índice para recorrer la cadena.
    char c;         // Variable para almacenar el carácter actual.

    // Mientras no se llegue al final de la cadena (es decir, mientras no sea el carácter nulo '\0').
    while (str[i])
    {
        c = str[i];  // Obtiene el carácter actual de la cadena.

        // Verifica si el carácter está en el rango de letras minúsculas ('a' a 'z').
        if (c >= 'a' && c <= 'z')
        {
            // Calcula el nuevo carácter aplicando ROT13.
            // (c - 'a') convierte 'a' en 0, 'b' en 1, ..., 'z' en 25.
            // Añade 13 para rotar, y % 26 asegura que vuelva al principio si se pasa de 'z'.
            // Luego, + 'a' convierte el índice de vuelta a un carácter en el rango de 'a' a 'z'.
            c = ((c - 'a' + 13) % 26) + 'a';
        }
        // Verifica si el carácter está en el rango de letras mayúsculas ('A' a 'Z').
        else if (c >= 'A' && c <= 'Z')
        {
            // Calcula el nuevo carácter aplicando ROT13.
            // (c - 'A') convierte 'A' en 0, 'B' en 1, ..., 'Z' en 25.
            // Añade 13 para rotar, y % 26 asegura que vuelva al principio si se pasa de 'Z'.
            // Luego, + 'A' convierte el índice de vuelta a un carácter en el rango de 'A' a 'Z'.
            c = ((c - 'A' + 13) % 26) + 'A';
        }
        // Escribe el carácter transformado en la salida estándar (generalmente la consola).
        write(1, &c, 1);
        i++;  // Avanza al siguiente carácter de la cadena.
    }
}

// Función principal que gestiona los argumentos y llama a la función de cifrado.
int main(int argc, char **argv)
{
    // Verifica si hay exactamente dos argumentos (el programa y una cadena de texto).
    if (argc == 2)
    {
        rot_13(argv[1]);  // Llama a la función rot_13 con la cadena de texto proporcionada.
    }
    // Imprime un salto de línea al final de la salida para asegurar el formato adecuado.
    write(1, "\n", 1);
    return 0;  // Devuelve 0 para indicar que el programa se ejecutó correctamente.
} */
