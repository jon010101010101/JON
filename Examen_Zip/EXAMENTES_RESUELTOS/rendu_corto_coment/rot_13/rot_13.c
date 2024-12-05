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

#include <unistd.h>  // Librería para el uso de la función write

#define SU argv[1][i]  // Macro para simplificar el acceso a argv[1][i]

int main(int argc, char **argv)
{
    // Comprobamos si se pasa exactamente un argumento en la línea de comandos
    if (argc == 2)
    {
        int i = 0;  // Inicializamos un índice para recorrer la cadena de caracteres

        // Recorremos la cadena de caracteres hasta el final ('\0')
        while (SU)
        {
            // Si el carácter está entre 'a' y 'm' o 'A' y 'M', aplicamos el ROT13 sumando 13
            if ((SU >= 'a' && SU <= 'm') || (SU >= 'A' && SU <= 'M'))
                SU = SU + 13;
            // Si el carácter está entre 'n' y 'z' o 'N' y 'Z', aplicamos el ROT13 restando 13
            else if ((SU >= 'n' && SU <= 'z') || (SU >= 'N' && SU <= 'Z'))
                SU = SU - 13;

            // Escribimos el carácter modificado en la salida estándar
            write(1, &SU, 1);
            i++;  // Avanzamos al siguiente carácter
        }
    }
    // Escribimos un salto de línea al final
    write(1, "\n", 1);
    return (0);  // Devolvemos 0 indicando que el programa terminó correctamente
}


