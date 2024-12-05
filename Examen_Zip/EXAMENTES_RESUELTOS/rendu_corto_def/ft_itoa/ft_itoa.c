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

/* FUNCIONA Y PASA MAQUINA */

#include <stdlib.h>
#include <limits.h> 

int ft_count(int nbr)
{
    int count = (nbr <= 0); // Inicializa en 1 si el número es 0 o negativo

    while (nbr)
    {
        nbr /= 10;
        count++;
    }
    return (count);
}

char	*ft_itoa(int nbr)
{
	long	num;
	int		len;
	char	*digits;
	char	*newstr;

	num = nbr;
	len = ft_count(nbr);
	digits = "0123456789";
	newstr = (char *)malloc(sizeof(char) * (len + 1));
	if(!newstr)
		return (NULL);
	newstr[len] = '\0';
	len = len - 1;
	if (num == 0)
		newstr[0] = '0';
	if (num < 0)
	{
		newstr[0] = '-';
		num = -num;
	}
	while (num != 0)
	{
		newstr[len] = digits[num % 10];
		num = num /10;
		len --; 
	}
	return (newstr);
}

#include <stdio.h>
#include <limits.h>

int main(void)
{
    char *str;

    str= ft_itoa(INT_MIN);
    printf("%s\n", str);
    free(str);

    str= ft_itoa(INT_MAX);
    printf("%s\n", str);
    free(str);

    str= ft_itoa(0);
    printf("%s\n", str);
    free(str);

    return(0);
}


/* FUNCIONA PERO NO PASA MAQUINA IÑAKI */
/* #include <unistd.h>
#include <stdio.h>

char *ft_itoa(int nbr)
{
    static char str[12]; // digit max 11 + 0
    char temp[12];
    int i = 0;
    int j = 0;
    long n = nbr;

    if (n == 0)
	{
        str[0] = '0';
        str[1] = '\0';
        return (str);
    }
    if (n < 0)
	{
        n = -n;
        str[j++] = '-';
    }
    while (n > 0)
	{
        temp[i++] = (n % 10) + '0';
        n /= 10;
    }
    while (i > 0)
	{
        str[j++] = temp[--i];
    }
    str[j] = '\0';
    return (str);
} */

#include <stdio.h>

int main(void)
{
    printf("ft_itoa(-2147483648) = %s\n", ft_itoa(-2147483648));
    printf("ft_itoa(2147483647) = %s\n", ft_itoa(2147483647));
    printf("ft_itoa(0) = %s\n", ft_itoa(0));
    printf("ft_itoa(-1) = %s\n", ft_itoa(-1));
    printf("ft_itoa(1) = %s\n", ft_itoa(1));
    printf("ft_itoa(-42) = %s\n", ft_itoa(-42));
    printf("ft_itoa(123456) = %s\n", ft_itoa(123456));
    printf("ft_itoa(123456789) = %s\n", ft_itoa(123456789));
    printf("ft_itoa(-123456789) = %s\n", ft_itoa(-123456789));
    printf("ft_itoa(987654321) = %s\n", ft_itoa(987654321));
    printf("ft_itoa(-987654321) = %s\n", ft_itoa(-987654321));
    printf("ft_itoa(10) = %s\n", ft_itoa(10));
    printf("ft_itoa(-10) = %s\n", ft_itoa(-10));
    printf("ft_itoa(100000) = %s\n", ft_itoa(100000));
    printf("ft_itoa(-100000) = %s\n", ft_itoa(-100000));
    printf("ft_itoa(999) = %s\n", ft_itoa(999));
    printf("ft_itoa(-999) = %s\n", ft_itoa(-999));
    
    return (0);
}
