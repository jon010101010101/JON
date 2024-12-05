
#include <unistd.h>
#include <stdio.h>

int ft_strlen(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')  // Recorro el argumento
        i++;                // Aumento el contador        
    return (i);             // Devuelvo el contador
}

/*
int main(void)
{
    printf("%d", ft_strlen("Hola Mundo"));
    return (0);
} 
*/


/* Assignment name  : ft_strlen
Expected files   : ft_strlen.c
Allowed functions: 
--------------------------------------------------------------------------------
Write a function that returns the length of a string.
Your function must be declared as follows:
int	ft_strlen(char *str);
--------------------------------------------------------------------------------
Escribe una función que devuelva la longitud de una cadena.
Su función debe declararse de la siguiente manera:
int ft_strlen(char *str); */