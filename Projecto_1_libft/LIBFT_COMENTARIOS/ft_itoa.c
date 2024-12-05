/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/19 12:07:34 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:53:38 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*handle_zero_case(void)
{
	char	*result_zero;

	result_zero = (char *)malloc(2 * sizeof(char));
	if (result_zero == 0)
		return (NULL);
	result_zero[0] = '0';
	result_zero[1] = '\0';
	return (result_zero);
}

void	extract_sign_and_number(int n, int *sign, long long *num)
{
	if (n < 0)
	{
		*sign = -1;
		*num = -(long long)n;
	}
	else
	{
		*sign = 1;
		*num = n;
	}
}

char	*convert_number_to_str(long long num, int size, int sign)
{
	char	*result;

	result = (char *)malloc((size + 1) * sizeof(char));
	if (result == NULL)
		return (NULL);
	result[size] = '\0';
	while (size > 0)
	{
		result[size - 1] = num % 10 + '0';
		num = num / 10;
		size--;
	}
	if (sign == -1)
		result[0] = '-';
	return (result);
}

char	*ft_itoa(int n)
{
	int			sign;
	long long	num;
	int			size;
	long long	temp;

	if (n == 0)
		return (handle_zero_case());
	extract_sign_and_number(n, &sign, &num);
	size = 0;
	temp = num;
	while (temp > 0)
	{
		temp = temp / 10;
		size++;
	}
	if (sign == -1)
		size++;
	return (convert_number_to_str(num, size, sign));
}

/*
int	main(void)
{
	int		num;
	char	*str;

	num = 2147483647;
	str = ft_itoa(num);
	if (str != NULL)
	{
		printf("Número: %d, Cadena: %s\n", num, str);
		free(str);
	}
	num = -2147483648;
	str = ft_itoa(num);
	if (str != NULL)
	{
		printf("Número: %d, Cadena: %s\n", num, str);
		free(str);
	}
	return (0);
}
*/

// DESCRIPCION.Utilizando malloc(3), genera una string que represente
// el valor entero recibido como argumento. Los números negativos
// tienen que gestionarse.

// VALOR DEVUELTO. La string que represente el número. NULL si falla la
// reserva de memoria.

// PARAMETROS
// n: el entero a convertir.

/* La función ft_itoa convierte un número entero n en una cadena de 
caracteres correspondiente a su representación en base 10. 

1-Determinación de la longitud de la cadena resultante contando el 
	número de dígitos en el número entero n
2-Asignación de memoria para la nueva cadena utilizando malloc, 
	con un tamaño igual a la longitud calculada más uno para el carácter nulo \0.
3-Conversión del número entero en una cadena de caracteres. La función
	convierte cada dígito del número entero n en un carácter, empezando por 
	el último dígito y avanzando hacia la izquierda
4-Manejo del signo del número. Si n es negativo, se coloca el signo - 
	al principio de la cadena y se convierte el valor absoluto de n.
5- Inversión de la cadena. Una vez que todos los dígitos se han agregado 
	a la cadena, esta se invierte para que los dígitos estén en el orden 
	correcto
6-Devolver la nueva cadena: La función devuelve la nueva 
	cadena que contiene la representación de n en formato de caracteres
 */

/* EJEMPLO
Vamos a desglosar y explicar paso a paso cómo funciona cada parte del código 
para convertir un número entero int n a su representación en cadena de caracteres
 (char *). Este es un proceso detallado para comprender la implementación de la 
 función ft_itoa.

1. FUNCION HANDLE_ZERO_CASE
Esta función maneja el caso especial en que el número n es 0.

char *handle_zero_case(void)
{
    char *result_zero;

    result_zero = (char *)malloc(2 * sizeof(char));
    if (result_zero == 0)
        return (NULL);
    result_zero[0] = '0';
    result_zero[1] = '\0';
    return (result_zero);
}
1. Paso a Paso:
	Asignar memoria:

	result_zero = (char *)malloc(2 * sizeof(char));
	Se asigna memoria para 2 caracteres: uno para el dígito '0' y otro para el 
	carácter nulo '\0'.

2. Comprobar asignación de memoria:

if (result_zero == 0)
    return (NULL);
Si malloc falla, retorna NULL.

3. Inicializar la cadena:

result_zero[0] = '0';
result_zero[1] = '\0';

4. Retornar la cadena:

return (result_zero);


2. FUNCION EXTRACT SIGN AND NUMBER
Esta función determina el signo del número y lo convierte a un número positivo 
si es negativo.

void extract_sign_and_number(int n, int *sign, long long *num)
{
    if (n < 0)
    {
        *sign = -1;
        *num = -(long long)n;
    }
    else
    {
        *sign = 1;
        *num = n;
    }
}
Paso a Paso:
1. Determinar el signo y el valor absoluto:

if (n < 0)
{
    *sign = -1;
    *num = -(long long)n;
}
else
{
    *sign = 1;
    *num = n;
}
Si n es negativo, el signo es -1 y *num se convierte al valor positivo 
equivalente.
Si n es positivo, el signo es 1 y *num se mantiene igual.

3. FUNCION CONVERT NUMBER TO STR
Esta función convierte un número positivo num a su representación en cadena,
 incluyendo el signo si es negativo.

char *convert_number_to_str(long long num, int size, int sign)
{
    char *result;

    result = (char *)malloc((size + 1) * sizeof(char));
    if (result == NULL)
        return (NULL);
    result[size] = '\0';
    while (size > 0)
    {
        result[size - 1] = num % 10 + '0';
        num = num / 10;
        size--;
    }
    if (sign == -1)
        result[0] = '-';
    return (result);
}
Paso a Paso:
1. Asignar memoria:

result = (char *)malloc((size + 1) * sizeof(char));
Se asigna memoria para size caracteres más uno adicional para el carácter nulo 
'\0'.

2. Comprobar asignación de memoria:

if (result == NULL)
    return (NULL);
	
3. Inicializar el carácter nulo:

result[size] = '\0'; *****VER

4. Convertir el número a cadena:

while (size > 0)
{
    result[size - 1] = num % 10 + '0';
    num = num / 10;
    size--;
}
Mientras size sea mayor que 0, se extrae el último dígito de num (usando 
num % 10), se convierte a carácter y se almacena en result.
Se reduce size y se divide num por 10 para eliminar el último dígito.

5. Añadir el signo si es necesario:

if (sign == -1)
    result[0] = '-';
	
6. Retornar la cadena:

return (result);

******VER

Vamos a ver un ejemplo con el número -123.

Inicialización y Conteo de Dígitos
Supongamos que num = 123 y sign = -1. size se ha calculado como 4 (3 dígitos más
1 para el signo).

Asignar Memoria:

result = (char *)malloc((4 + 1) * sizeof(char)); // result tiene espacio para 5 
caracteres.
Inicializar el Carácter Nulo:

result[4] = '\0'; // Coloca el carácter nulo al final.
Llenar la Cadena en Orden Inverso:

Primera Iteración:

result[3] = 123 % 10 + '0'; // '3'
num = 123 / 10; // 12
size--; // size es 3
Segunda Iteración:

result[2] = 12 % 10 + '0'; // '2'
num = 12 / 10; // 1
size--; // size es 2
Tercera Iteración:

result[1] = 1 % 10 + '0'; // '1'
num = 1 / 10; // 0
size--; // size es 1
Finalización del Bucle:

size es 0, se sale del bucle.
Agregar el Signo:

if (sign == -1)
    result[0] = '-'; // La cadena ahora es "-123".
	
Resultado Final
La cadena result es "-123", con '\0' al final para indicar el final de la 
cadena.

Resumen
La línea result[size] = '\0'; asegura que la cadena resultante esté 
correctamente terminada con un carácter nulo. Esto es esencial para que 
cualquier función que maneje la cadena pueda determinar su longitud 
correctamente y evitar leer más allá  del final del arreglo de caracteres,
 evitando así un comportamiento indefinido y posibles errores.

4. FUNCION FT_ITOA
Esta función principal coordina todo el proceso para convertir un número
 entero a cadena de caracteres.

char *ft_itoa(int n)
{
    int sign;
    long long num;
    int size;
    long long temp;

    if (n == 0)
        return (handle_zero_case());
    extract_sign_and_number(n, &sign, &num);
    size = 0;
    temp = num;
    while (temp > 0)
    {
        temp = temp / 10;
        size++;
    }
    if (sign == -1)
        size++;
    return (convert_number_to_str(num, size, sign));
}
Paso a Paso:
1. Comprobar si n es cero:

if (n == 0)
    return (handle_zero_case());
Si n es 0, se maneja el caso especial usando handle_zero_case.

2. Extraer el signo y el número positivo:

extract_sign_and_number(n, &sign, &num);

3.Determinar el tamaño de la cadena:

size = 0;
temp = num;
while (temp > 0)
{
    temp = temp / 10;
    size++;
}
if (sign == -1)
    size++;
Se inicializa size a 0.
Se usa una copia temporal de num para contar los dígitos.
Cada vez que se divide temp por 10, se incrementa size.
Si el signo es negativo, se incrementa size una vez más para el carácter '-'.

4. Convertir el número a cadena:

return (convert_number_to_str(num, size, sign));
Se llama a convert_number_to_str con num, size y sign para obtener la cadena 
resultante.

Resumen del Proceso

- Casos especiales: Si el número es 0, manejarlo por separado.
- Extraer información: Determinar el signo y convertir el número a positivo si
	 es necesario.
- Contar dígitos: Contar cuántos dígitos tiene el número.
- Convertir a cadena: Convertir el número y el signo a una cadena de caracteres.
- Retornar la cadena: Devolver la cadena resultante.

Este proceso asegura que el número entero n se convierta correctamente a su 
representación  en cadena, manejando tanto números positivos como negativos, 
incluyendo el caso  especial de cero. */
