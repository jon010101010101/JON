/*Escribe un programa que tome cadenas como argumentos y muestre su primer
argumento seguido de un \n.
Si el número de argumentos es menor que 1, el programa muestra \n.

Example:
$> ./aff_first_param vincent mit "l'ane" dans un pre et "s'en" vint | cat -e
vincent$
$> ./aff_first_param "j'aime le fromage de chevre" | cat -e
j'aime le fromage de chevre$
$> ./aff_first_param | cat -e
$*/

#include <unistd.h> // Incluye la biblioteca para usar la función write

int main (int argc, char **argv)
{
    int i = 0; // Declaración e inicialización del índice para recorrer la cadena de caracteres

    // Verifica si se ha proporcionado al menos un argumento adicional
    if (argc > 1)
    {
        // Itera sobre los caracteres de argv[1] (el primer argumento pasado al programa)
        // hasta encontrar el carácter nulo '\0' que marca el final de la cadena
        while(argv[1][i] != '\0')
            // Imprime el carácter actual de argv[1] usando write
            write(1, &argv[1][i++], 1); // Incrementa 'i' después de cada impresión
    }
    // Imprime un salto de línea después de procesar el argumento
    write(1, "\n", 1);

    return (0); // Retorna 0 para indicar que el programa ha finalizado correctamente
}
