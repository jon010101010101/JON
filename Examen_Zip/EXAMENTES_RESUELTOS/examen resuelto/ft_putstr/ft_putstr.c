#include <unistd.h>

void ft_putstr(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')          // Recorro el argumento
        write(1, &str[i++], 1);     // Escribo el carácter y Aumento el contador para recorrer el argumento
}


/* int main(void)
{
    ft_putstr("Hola que tal");
    return (0);
} */

/*  Assignment name  : ft_putstr
 Expected files   : ft_putstr.c
 Allowed functions: write
 --------------------------------------------------------------------------------
 Write a function that displays a string on the standard output.
 The pointer passed to the function contains the address of the string's first
 character.
 Your function must be declared as follows:
 void	ft_putstr(char *str);
 --------------------------------------------------------------------------------
Escribe una función que muestre una cadena en la salida estándar.
El puntero pasado a la función contiene la dirección del primer caracter de la
cadena.
Su función debe declararse de la siguiente manera:
void ft_putstr(char *str); */