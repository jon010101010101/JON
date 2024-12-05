/*Escribe una función que devuelva la longitud de una cadena.
Su función debe declararse de la siguiente manera:
int ft_strlen(char *str);*/

int ft_strlen(char *str)
{
    int     i = 0;
    
    while (str[i] != '\0')
        i++;
    return (i);       
}
