/*Escribe un programa que tome una cadena y muestre la primera 'z'
carácter que encuentra en él, seguido de una nueva línea. si no hay
caracteres 'z' en la cadena, el programa escribe 'z' seguido
por una nueva línea. Si el número de parámetros no es 1, el programa muestra
'z' seguida de una nueva línea.

Example:
$> ./aff_z "abc" | cat -e
z$
$> ./aff_z "dubO a POIL" | cat -e
z$
$> ./aff_z "zaz sent le poney" | cat -e
z$
$> ./aff_z | cat -e
z$
*/
#include <unistd.h>

int main(void)
{
	write(1, "z\n", 2);
	return (0);
}