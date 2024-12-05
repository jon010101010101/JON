/*
Assignment name  : rotone
Expected files   : rotone.c
Allowed functions: write
--------------------------------------------------------------------------------
Write a program that takes a string and displays it, replacing each of its
letters by the next one in alphabetical order.
'z' becomes 'a' and 'Z' becomes 'A'. Case remains unaffected.
The output will be followed by a \n.
If the number of arguments is not 1, the program displays \n.
-------------------------------------------------- ------------------------------
Escribe un programa que tome una cadena y la muestre, reemplazando cada uno de sus
letras por la siguiente en orden alfabético.
'z' se convierte en 'a' y 'Z' se convierte en 'A'. El caso no se ve afectado.
La salida irá seguida de un \n.
Si el número de argumentos no es 1, el programa muestra \n.

Example:
$>./rotone "abc"
bcd
$>./rotone "Les stagiaires du staff ne sentent pas toujours tres bon." | cat -e
Mft tubhjbjsft ev tubgg of tfoufou qbt upvkpvst usft cpo.$
$>./rotone "AkjhZ zLKIJz , 23y " | cat -e
BlkiA aMLJKa , 23z $
$>./rotone | cat -e
$
$>
$>./rotone "" | cat -e
$
$>
*/

/* SANDRA OK*/

#include <unistd.h>

int main(int argc, char **argv)
{
	if (argc == 2)
	{
		int i = 0;
		while (argv[1][i] != '\0')
		{
			if ((argv[1][i] >= 'a' && argv[1][i] < 'z') || (argv[1][i] >= 'A' && argv[1][i] < 'Z'))
				argv[1][i] = argv[1][i] + 1;
			else if (argv[1][i] == 'z')
				argv[1][i] = 'a';
			else if (argv[1][i] == 'Z')
				argv[1][i] = 'A';
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
/* ANA OK*/

/* #include <unistd.h>

int main(int argc, char **argv)
{
	int i;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if ((argv[1][i] >= 'a' && argv[1][i] < 'z') || (argv[1][i] >= 'A' && argv[1][i] < 'Z'))
			{
				argv[1][i] = argv[1][i] + 1;
			}
			else if (argv[1][i] ==  'z')
			{
				argv[1][i] = 'a';
			}
			else if (argv[1][i] == 'Z') 
			{
				argv[1][i] = 'A';
			
			}
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
} */

/* COMENTARIOS ANA*/
/* #include <unistd.h>   // Incluimos la biblioteca unistd.h para usar la función write

int main(int argc, char **argv)
{
    int i;

    i = 0;  // Inicializamos el índice i a 0 para recorrer la cadena

    // Verificamos que se haya pasado exactamente un argumento adicional al programa
    if (argc == 2)
    {
        // Recorremos la cadena de caracteres mientras no lleguemos al final ('\0')
        while (argv[1][i])
        {
            // Condición para letras minúsculas 'a' a 'y' y mayúsculas 'A' a 'Y'
            if ((argv[1][i] >= 'a' && argv[1][i] < 'z') || (argv[1][i] >= 'A' && argv[1][i] < 'Z'))
            {
                // Desplazamos el carácter al siguiente en el alfabeto
                argv[1][i] = argv[1][i] + 1;
            }
            // Condición especial para la letra 'z'
            else if (argv[1][i] == 'z')
            {
                // Convertimos 'z' en 'a'
                argv[1][i] = 'a';
            }
            // Condición especial para la letra 'Z'
            else if (argv[1][i] == 'Z')
            {
                // Convertimos 'Z' en 'A'
                argv[1][i] = 'A';
            }

            // Escribimos el carácter modificado o no en la salida estándar
            write(1, &argv[1][i], 1);

            // Incrementamos el índice i para pasar al siguiente carácter
            i++;
        }
    }

    // Escribimos un salto de línea en la salida estándar
    write(1, "\n", 1);

    // Retornamos 0 para indicar que el programa terminó con éxito
    return (0);
} */


/* #include <unistd.h>

void rotone(char *str)
{
    int i = 0;
    char c;

    while (str[i])
    {
        c = str[i];
        if (c >= 'a' && c <= 'z')
        {
            if (c == 'z')
                c = 'a';
            else
                c = c + 1;
        }
        else if (c >= 'A' && c <= 'Z')
        {
            if (c == 'Z')
                c = 'A';
            else
                c = c + 1;
        }
        write(1, &c, 1);
        i++;
    }
    write(1, "\n", 1);
}

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        rotone(argv[1]);
    }
    else
    {
        write(1, "\n", 1);
    }
    return (0);
} */

/* #include <unistd.h>  // Incluye la biblioteca que proporciona la función 'write'.

// Función que aplica un desplazamiento de +1 en el alfabeto a cada carácter en la cadena.
void rotone(char *str)
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
            // Si el carácter es 'z', se convierte en 'a' (rotación al inicio del alfabeto).
            if (c == 'z')
                c = 'a';
            else
                // De lo contrario, se incrementa el carácter en 1 posición en el alfabeto.
                c = c + 1;
        }
        // Verifica si el carácter está en el rango de letras mayúsculas ('A' a 'Z').
        else if (c >= 'A' && c <= 'Z')
        {
            // Si el carácter es 'Z', se convierte en 'A' (rotación al inicio del alfabeto).
            if (c == 'Z')
                c = 'A';
            else
                // De lo contrario, se incrementa el carácter en 1 posición en el alfabeto.
                c = c + 1;
        }

        // Escribe el carácter transformado en la salida estándar (generalmente la consola).
        write(1, &c, 1);
        i++;  // Avanza al siguiente carácter de la cadena.
    }
 */

