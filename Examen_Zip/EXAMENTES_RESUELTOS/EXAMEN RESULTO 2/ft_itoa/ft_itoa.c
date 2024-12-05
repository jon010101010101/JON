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

/* #include <stdlib.h>

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
#include <stdio.h>
int	main(void)
{
 	int prueba = -2147483648;
 	char *str = ft_itoa(prueba);
 	printf("%s", str);
 	return(0);
} */

/* ANA */

/* #include <stdlib.h>
#include <limits.h> 

int	ft_count(int nbr)
{
	int	count;

	count = 0;
	if (nbr == 0)
		return (1);
	if (nbr < 0)
	{
		nbr = -nbr;
		count++;
	}
	while (nbr != 0)
	{
		nbr = nbr / 10;
		count++;
	}
	return(count);
}

char	*ft_itoa(int nbr)
{
	long	num;
	int		len;
	char	*digits;
	char	*newstring;

	num = nbr;
	len = ft_count(nbr);
	digits = "0123456789";
	newstring = (char *)malloc(sizeof(char) * (len + 1));
	if(!newstring)
		return (NULL);
	newstring[len] = '\0';
	len = len - 1;
	if (num == 0)
		newstring[0] = '0';
	if (num < 0)
	{
		newstring[0] = '-';
		num = -num;
	}
	while (num != 0)
	{
		newstring[len] = digits[num % 10];
		num = num /10;
		len --;
	}
	return (newstring);
}

int	main(void)
{
	int	prueba = 124;
	char *str;

	str = ft_itoa(prueba);
	printf("%d\n", ft_count(prueba));
	printf("%s\n", str);
	return (0);
} */
/* COMENTARIOS */

/* #include <stdlib.h>  // Incluimos la biblioteca stdlib.h para usar la función malloc
#include <limits.h>  // Incluimos limits.h para acceder a los límites de los tipos enteros (por si necesitamos valores como INT_MAX o INT_MIN)

int	ft_count(int nbr)
{
	int	count;

	count = 0;  // Inicializamos el contador en 0

	// Si el número es 0, retornamos 1 ya que 0 tiene una longitud de 1 carácter
	if (nbr == 0)
		return (1);

	// Si el número es negativo, lo convertimos a positivo y aumentamos el contador en 1 (para el signo '-')
	if (nbr < 0)
	{
		nbr = -nbr;
		count++;
	}

	// Este bucle cuenta cuántos dígitos tiene el número
	while (nbr != 0)
	{
		nbr = nbr / 10;  // Dividimos el número por 10 para eliminar el último dígito
		count++;  // Incrementamos el contador por cada dígito
	}

	// Retornamos la cantidad de dígitos (incluyendo el signo si el número es negativo)
	return(count);
}

char	*ft_itoa(int nbr)
{
	long	num;       // Usamos un long para evitar problemas con el límite inferior de los int
	int		len;       // Variable que almacena la longitud del número (cantidad de dígitos)
	char	*digits;   // Puntero a una cadena que contiene los dígitos '0' a '9'
	char	*newstring;  // Puntero para la cadena que contendrá la representación del número

	num = nbr;  // Copiamos el valor del número a la variable num
	len = ft_count(nbr);  // Calculamos la longitud del número usando ft_count
	digits = "0123456789";  // Asignamos la cadena de dígitos (tabla de conversión)

	// Reservamos memoria para la nueva cadena, incluyendo espacio para el carácter nulo ('\0')
	newstring = (char *)malloc(sizeof(char) * (len + 1));
	
	// Si malloc falla, retornamos NULL
	if (!newstring)
		return (NULL);
	
	newstring[len] = '\0';  // Asignamos el carácter nulo al final de la cadena
	len = len - 1;  // Ajustamos len para usarlo como índice en la cadena

	// Si el número es 0, directamente asignamos '0' como primer carácter
	if (num == 0)
		newstring[0] = '0';

	// Si el número es negativo, asignamos el signo '-' y convertimos num a positivo
	if (num < 0)
	{
		newstring[0] = '-';
		num = -num;
	}

	// Convertimos el número a su representación en cadena, desde el final hacia el principio
	while (num != 0)
	{
		newstring[len] = digits[num % 10];  // Asignamos el dígito correspondiente
		num = num / 10;  // Eliminamos el último dígito del número
		len--;  // Retrocedemos en el índice para llenar el siguiente dígito
	}

	// Retornamos la cadena resultante
	return (newstring);
}

int	main(void)
{
	int	prueba = 124;  // Declaramos un número de prueba
	char *str;  // Declaramos un puntero para la cadena resultante

	str = ft_itoa(prueba);  // Convertimos el número a cadena usando ft_itoa
	printf("%d\n", ft_count(prueba));  // Imprimimos la cantidad de dígitos (o longitud) del número
	printf("%s\n", str);  // Imprimimos la cadena resultante
	return (0);  // Terminamos el programa con éxito
} */
/* #include <stdlib.h>
#include <stdio.h>

// Calcula la longitud necesaria para representar el número en una cadena.
int nlen(long nbr)
{
    int len = 0;
    if (nbr <= 0)
        len++;  // Para el signo '-' o '0'
    while (nbr != 0)
    {
        len++;
        nbr = nbr / 10;
    }
    return (len);
}

// Convierte un número entero en una cadena de caracteres.
char *ft_itoa(int nbr)
{
    char *digits = "0123456789";
    long n = nbr;
    int len = nlen(n);
    char *str = (char *)malloc(sizeof(char) * (len + 1)); // +1 para el carácter nulo
    if (!str)
        return NULL;

    str[len] = '\0';  // Termina la cadena con un carácter nulo.

    // Manejo de números negativos
    if (n < 0)
    {
        str[0] = '-';
        n = -n;
    }

    // Manejo del número 0
    if (n == 0)
    {
        str[0] = '0';
        return (str);
    }

    // Llena la cadena desde el final hacia el principio
    while (n != 0)
    {
        str[--len] = digits[n % 10];
        n = n / 10;
    }

    return (str);
}

int main(void)
{
    int prueba = -2147483648; // Prueba con el valor específico
    char *str = ft_itoa(prueba);
    if (str)
    {
        printf("%s", str);
        free(str);  // Libera la memoria al finalizar.
    }
    else
    {
        printf("Error allocating memory.\n");
    }
    return (0);
} */
/* COMENTARIOS */

/* #include <stdlib.h>
#include <stdio.h>

// Calcula la longitud necesaria para representar el número en una cadena.
int nlen(long nbr)
{
    int len = 0;

    // Si el número es negativo o cero, incrementa la longitud inicial
    if (nbr <= 0)
        len++;  // Para el signo '-' o '0'
    
    // Calcula la longitud del número en dígitos
    while (nbr != 0)
    {
        len++;
        nbr = nbr / 10; // Elimina el dígito menos significativo
    }
    return (len);
}

// Convierte un número entero en una cadena de caracteres.
char *ft_itoa(int nbr)
{
    char *digits = "0123456789"; // Cadena de caracteres para representar los dígitos
    long n = nbr;  // Usamos 'long' para manejar el caso especial -2147483648
    int len = nlen(n);  // Calcula la longitud necesaria para la cadena
    char *str = (char *)malloc(sizeof(char) * (len + 1)); // +1 para el carácter nulo

    // Verifica si la asignación de memoria fue exitosa
    if (!str)
        return NULL;

    str[len] = '\0';  // Termina la cadena con un carácter nulo.

    // Manejo de números negativos
    if (n < 0)
    {
        str[0] = '-';  // Coloca el signo '-' al principio
        n = -n;  // Convierte el número a positivo para el procesamiento
    }

    // Manejo del número 0
    if (n == 0)
    {
        str[0] = '0';  // Asigna '0' si el número es 0
        return str;  // Devuelve la cadena con el único carácter '0'
    }

    // Llena la cadena desde el final hacia el principio
    while (n != 0)
    {
        str[--len] = digits[n % 10];  // Coloca el dígito en la posición actual
        n = n / 10;  // Elimina el dígito menos significativo
    }

    return str;  // Devuelve la cadena resultante
}

int main(void)
{
    int prueba = -2147483648; // Prueba con el valor específico
    char *str = ft_itoa(prueba);  // Convierte el número en una cadena

    // Verifica si la conversión fue exitosa
    if (str)
    {
        printf("%s\n", str);  // Imprime la cadena resultante
        free(str);  // Libera la memoria asignada para la cadena
    }
    else
    {
        printf("Error allocating memory.\n");  // Mensaje de error si la asignación falla
    }
    return 0;
} */
#include <unistd.h>
#include <stdio.h>

#define MAX_DIGITS 12  // Máximo de dígitos para un entero de 32 bits y el signo negativo

char *ft_itoa(int nbr)
{
    static char str[MAX_DIGITS];  // Usamos un arreglo estático para almacenar el resultado
    char temp[MAX_DIGITS];  // Arreglo temporal para construir el número en orden inverso
    int i = 0;
    int j = 0;
    long n = nbr;  // Convertimos a 'long' para manejar correctamente los casos extremos

    // Manejar el caso de número cero explícitamente
    if (n == 0)
	{
        str[0] = '0';
        str[1] = '\0';
        return (str);
    }

    // Manejar el caso de números negativos
    if (n < 0)
	{
        n = -n;  // Convertir a positivo para el procesamiento adicional
        str[j++] = '-';  // Agregar el signo negativo al principio de la cadena
    }

    // Convertir el número a cadena de caracteres (en orden inverso)
    while (n > 0)
	{
        temp[i++] = (n % 10) + '0';  // Obtener el último dígito y almacenarlo como un carácter
        n /= 10;  // Reducir el número dividiendo por 10
    }

    // Invertir la cadena de 'temp' a 'str', después del signo negativo si existe
    while (i > 0)
	{
        str[j++] = temp[--i];
    }

    str[j] = '\0';  // Terminar la cadena final con un carácter nulo

    return (str);
}

int main(void)
{
    int number = -2147483648;  // Caso límite
    char *str;

    str = ft_itoa(number);
    printf("%s\n", str);  // La salida debería ser: -2147483648

    return (0);
}

