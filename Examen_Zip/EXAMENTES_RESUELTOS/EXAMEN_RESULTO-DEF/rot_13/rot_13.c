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

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        char SU;

        while (argv[1][i])
        {
            SU = argv[1][i]; // Asigna el carácter actual a SU

            if ((SU >= 'a' && SU <= 'm') || (SU >= 'A' && SU <= 'M')) {
                SU += 13; // Aplica ROT13 a SU
            } else if ((SU >= 'n' && SU <= 'z') || (SU >= 'N' && SU <= 'Z')) {
                SU -= 13; // Aplica ROT13 a SU
            }

            write(1, &SU, 1); // Imprime el carácter modificado
            i++;
        }
    }
    write(1, "\n", 1); // Imprime un salto de línea al final
    return (0);
}


/* SANDRA OK*/

/* #include <unistd.h>

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
} */
/* FUNCIONA */

/* #include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        char ch = argv[1][i];

        while (ch)
        {
            // Aplica ROT13 al carácter
            if ((ch >= 'a' && ch <= 'z'))
            {
                if (ch >= 'a' && ch <= 'm')
                    ch += 13;
                else
                    ch -= 13;
            } else if ((ch >= 'A' && ch <= 'Z'))
            {
                if (ch >= 'A' && ch <= 'M')
                    ch += 13;
                else
                    ch -= 13;
            }
            // Imprime el carácter modificado
            write(1, &ch, 1);
            i++;
            ch = argv[1][i]; // Avanza al siguiente carácter
        }
    }
    
    write(1, "\n", 1); // Imprime una nueva línea al final
    return 0;
} */
