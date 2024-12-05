/*jon funciona y pasa*/
#include <stdlib.h>
#include <limits.h> 

int	nlen(int nbr)
{
	int n = 0;
	if (nbr <= 0)
		n++;
	while (nbr != 0)
	{
		n++;
		nbr = nbr / 10;
	}
	return (n);
	
}

char *ft_itoa(int nbr)
{
	char *digits = "0123456789";
    int len;

    if (nbr == INT_MIN)
    {
        char *min_int_str = (char *)malloc(12 * sizeof(char));
        if (!min_int_str)
            return NULL;
        min_int_str[0] = '-';
        min_int_str[1] = '2';
        min_int_str[2] = '1';
        min_int_str[3] = '4';
        min_int_str[4] = '7';
        min_int_str[5] = '4';
        min_int_str[6] = '8';
        min_int_str[7] = '3';
        min_int_str[8] = '6';
        min_int_str[9] = '4';
        min_int_str[10] = '8';
        min_int_str[11] = '\0';
        return min_int_str;
    }

    len = nlen(nbr);
    char *str = (char *)malloc(sizeof(char) * (len + 1));
    if (!str)
        return (NULL);
    str[len] = '\0';
    if (nbr < 0)
    {
        str[0] = '-';
        nbr = -nbr;
    }
    if (nbr == 0)
    {
        str[0] = '0';
    }
    while (nbr != 0)
    {
        str[len--] = digits[nbr % 10];
        nbr = nbr / 10;
    }
    return (str);
}


/*#include <stdio.h>

int main(void)
{
    printf("%s\n", ft_itoa(0));
    printf("%s\n", ft_itoa(-2147483648));
    printf("%s\n", ft_itoa(1));
    printf("%s\n", ft_itoa(12));
    printf("%s\n", ft_itoa(2147483647));
    printf("%s\n", ft_itoa(-4));
    printf("%s\n", ft_itoa(-23));
    return (0);
}
*/





/*JON COMPILA Y PARACE QUE VA BIEN PERO NO PASA*/

#include <stdlib.h>

int get_num_length(int nbr)
{
    int length = 0;
    if (nbr <= 0)
    {
        length = 1;
    }
    while (nbr != 0)
    {
        length++;
        nbr /= 10;
    }
    return (length);
}

char *ft_itoa(int nbr)
{
    int     length;
    char    *result;
    int     is_negative;

    length = get_num_length(nbr);
    result = (char *)malloc(sizeof(char) * (length + 1));
    if (!result)
        return (NULL);

    result[length] = '\0';
    is_negative = nbr < 0;

    if (nbr == 0)
    {
        result[0] = '0';
        return (result);
    }
    if (is_negative)
    {
        if (nbr == -2147483648)
        {
            result[0] = '-';
            result[1] = '2';
            nbr = 147483648;
        }
        else
        {
            nbr = -nbr;
        }
    }
    while (nbr != 0)
    {
        result[--length] = (nbr % 10) + '0';
        nbr /= 10;
    }
    if (is_negative && result[0] != '-')
    {
        result[0] = '-';
    }
    return (result);
}

/*#include <stdio.h>

int main(void)
{
    printf("%s\n", ft_itoa(0));
    printf("%s\n", ft_itoa(-2147483648));
    printf("%s\n", ft_itoa(1));
    printf("%s\n", ft_itoa(12));
    printf("%s\n", ft_itoa(2147483647));
    printf("%s\n", ft_itoa(-4));
    printf("%s\n", ft_itoa(-23));
    return (0);
}*/

/*SANDRA COMPILA Y PARACE QUE VA BIEN PERO NO PASA */
#include <stdlib.h>

int	nlen(int nbr)
{
	int n = 0;
	if (nbr <= 0)
		n++;
	while (nbr != 0)
	{
		n++;
		nbr = nbr / 10;
	}
	return (n);
}

char *ft_itoa(int nbr)
{
	char *digits = "0123456789";
	int	len = nlen(nbr);
	char *str = (char *)malloc(sizeof(char) * (len + 1));
	if (!str)
		return (NULL);
	if (nbr == -2147483648)
		return ("-2147483648\0");
	str[len] = '\0';
	if (nbr < 0)
	{
		str[0] = '-';
		nbr = nbr * -1;
	}
	if (nbr == 0)
	{
		str[0] = '0';
	}
	while (nbr != 0)
	{
		str[--len] = digits[nbr % 10];
		nbr = nbr / 10;
	}
	return (str);
}
/*
#include <stdio.h>

int	main(void)
{
    int prueba = -2147483648;
    char *str = ft_itoa(prueba);
    printf("%s", str);
    return(0);
}
*/


/*IÑAKI*/
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char *ft_strncpy(char *dest, const char *src, size_t n)
{
    size_t i;

    i = 0;
    while (i < n && src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
    return dest;
}

/*
LA FUNCION STRNCPY la puedes generar desde la ayuda:
man strncpy

char *
           strncpy(char *dest, const char *src, size_t n)
           {
               size_t i;

               for (i = 0; i < n && src[i] != '\0'; i++)
                   dest[i] = src[i];
               for ( ; i < n; i++)
                   dest[i] = '\0';

               return dest;
           }

TUNEALA añadiendo "ft_" y transformando los "for" en un simple while
*/

int ft_nbrlen(int nbr)      // Función para contar los digitos del número y el signo en caso de negativo
{
    int i;

    i = 0;
    if (nbr < 0)            // Si el número es menor de 0 (negativo)
    {
        i++;                // Cuento uno por el signo negativo
        nbr = nbr * (-1);   // convierto el número en positivo
    }
    while (nbr > 0)         // Recorro el número mientras sea mayor que 0
    {
        i++;                // Cuento el digito
        nbr = nbr / 10;     // Divido el número entre 10 (me muevo entre unidades, decenas, centenas...)
    }
    return(i);              // Devuelvo el número de digitos incluyendo el signo en caso de negativo
}

char *ft_itoa(int nbr)
{
    char    *myitoa;
    int     len;

    myitoa = "";
    len = 0;
    if (nbr == -2147483648)                             // Si nbr es igual a 2147483648 (debajo tienes un truco para obtener este número)
    {
        myitoa = (char *)malloc(sizeof(char) * 12);     // reservo memoria para los 11 carácteres y el cierre
        if (!myitoa)                                    // Protego el malloc
            return (NULL);
        myitoa[11] = '\0';                              // Cierro en la última posición
        ft_strncpy(myitoa, "-2147483648", 11);          // Copio 11 los carácteres con ft_strncpy
        return (myitoa);                                // Devuelvo el puntero al string
    }
    if (nbr == 0)                                       // Si nbr es igual a 0
    {
        myitoa = (char *)malloc(sizeof(char) * 2);      // reservo memoria para el carácter y el cierre
        if (!myitoa)                                    // Protego el malloc
            return (NULL);
        myitoa[1] = '\0';                               // Cierro en la última posición
        myitoa[0] = '0';                                // Asigno el carácter "0" en la primera posición
        return (myitoa);                                // Devuelvo el puntero al string
    }    
    char *digits = "0123456789";
    len = ft_nbrlen(nbr);                               // Obtengo el número de digitos y signo para reservar el tamaño
    myitoa = (char *)malloc(sizeof(char) * (len + 1));  // reservo memoria para el tamaño y el cierre
    if(!myitoa)                                         // Protego el malloc
        return (NULL);
    myitoa[len] = '\0';                                 // Cierro en la última posición
    if (nbr < 0)                                        // Si nbr es negativo
    {
        myitoa[0] = '-';                                // Agsino el signo "-" en la primera posición
        nbr = nbr * (-1);                               // convierto el número en positivo
    }
    while (nbr > 0)                                     // Recorro el número mientras sea mayor que 0
    {
        myitoa[--len] = digits[nbr % 10];               // Primero disminuyo el contador ya que esta en la ultima posición y luego asigno el digito obtenido del resto de la división entre 10. Pri
        nbr = nbr / 10;                                 // Divido el número entre 10 (me muevo entre unidades, decenas, centenas...)
    }
    return (myitoa);
}

/* 
int main(void)
{
    printf("%s\n", ft_itoa(0));
    printf("%s\n", ft_itoa(-2147483648));
    printf("%s\n", ft_itoa(1));
    printf("%s\n", ft_itoa(12));
    printf("%s\n", ft_itoa(2147483647));
    printf("%s\n", ft_itoa(-4));
    printf("%s\n", ft_itoa(-23));
    return (0);
}
*/


/*Assignment name  : ft_itoa
Expected files   : ft_itoa.c
Allowed functions: malloc
--------------------------------------------------------------------------------
Write a function that takes an int and converts it to a null-terminated string.
The function returns the result in a char array that you must allocate.
Your function must be declared as follows:
char	*ft_itoa(int nbr);
--------------------------------------------------------------------------------
Escribe una función que tome un int y lo convierta en una cadena terminada en nulo.
La función devuelve el resultado en una matriz de caracteres que debes asignar.
Su función debe declararse de la siguiente manera:
char *ft_itoa(int nbr);*/