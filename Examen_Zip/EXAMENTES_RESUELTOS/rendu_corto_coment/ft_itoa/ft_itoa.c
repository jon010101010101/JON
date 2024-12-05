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
    // Si el número es 0 o negativo, count se inicializa en 1, porque:
    // - Si es 0, la representación de "0" requiere al menos un dígito.
    // - Si es negativo, se necesitará espacio adicional para el signo '-'.
    int count = (nbr <= 0);

    // Este bucle divide el número entre 10 repetidamente para contar cuántos dígitos tiene.
    // El bucle se detiene cuando `nbr` se convierte en 0.
    while (nbr)
    {
        nbr /= 10;  // Divide el número por 10, eliminando el último dígito.
        count++;    // Incrementa el contador con cada dígito eliminado.
    }

    // Retorna el total de dígitos contados, incluyendo el signo si era negativo.
    return (count);
}


char	*ft_itoa(int nbr)
{
	long	num; // Usar long para manejar el caso INT_MIN
	int		len; // Longitud de la cadena resultante
	char	*digits; // String de caracteres dígitos
	char	*newstr;// Cadena resultante

	num = nbr; // Usar una variable long para manejar INT_MIN
	len = ft_count(nbr); // Contar los dígitos del número
	digits = "0123456789"; // Cadena de caracteres dígitos
	newstr = (char *)malloc(sizeof(char) * (len + 1)); // Asignar memoria para la cadena
	if(!newstr)
		return (NULL);
	newstr[len] = '\0'; // Terminar la cadena con un carácter nulo
	len = len - 1; // Ajustar el índice para el último carácter
	if (num == 0)
		newstr[0] = '0';
	if (num < 0)
	{
		newstr[0] = '-';// Añadir el signo negativo
		num = -num;// Convertir el número a positivo
	}
	while (num != 0)  // Convertir el número a la cadena de caracteres
	{
		newstr[len] = digits[num % 10]; // Obtener el dígito actual
		num = num /10; // Dividir el número por 10 para el siguiente dígito
		len --; 
	}
	return (newstr);
}



/* FUNCIONA PERO NO PASA MAQUINA IÑAKI */
#include <unistd.h>
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
}

/* int main(void)
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
} */
