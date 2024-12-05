#include <unistd.h>

void ft_putstr(char *str)
{
    int     i = 0;

    while(str[i] != '\0')
        write(1, &str[i++], 1);
}

/* int main(void)
{
    ft_putstr("Hola que tal");
    return (0);
} */

/*Escribe una función que muestre una cadena en la salida estándar.
El puntero pasado a la función contiene la dirección del primer caracter de la
cadena.
Su función debe declararse de la siguiente manera:
void ft_putstr(char *str);*/