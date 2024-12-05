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

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>

#define SU argv[1][i]

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;

        while (SU)
        {
            if ((SU >= 'a' && SU <= 'm') || (SU >= 'A' && SU <= 'M'))
                SU = SU + 13;
            else if ((SU >= 'n' && SU <= 'z') || (SU >= 'N' && SU <= 'Z'))
                SU = SU - 13;

            write(1, &SU, 1);
            i++;
        }
    }
    write(1, "\n", 1);
    return (0);
}
