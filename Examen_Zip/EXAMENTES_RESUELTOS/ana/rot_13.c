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
$>
*/

#include <unistd.h>

int main(int argc, char **argv)
{
	int i;

	i = 0;
	if (argc == 2)
	{
		while (argv[1][i])
		{
			if ((argv[1][i] >= 'a' && argv[1][i] <= 'm') || (argv[1][i] >= 'A' && argv[1][i] <= 'M'))
			{
				argv[1][i] = argv[1][i] + 13;
			}
			else if ((argv[1][i] > 'm' && argv[1][i] <= 'z') || (argv[1][i] > 'M' && argv[1][i] <= 'Z'))
			{
				argv[1][i] = argv[1][i] - 13;
			
			}
			write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}