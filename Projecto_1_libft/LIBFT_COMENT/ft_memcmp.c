/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 18:17:01 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:52:57 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*p1;
	unsigned char	*p2;

	p1 = (unsigned char *)s1;
	p2 = (unsigned char *)s2;
	if (n == 0)
		return (0);
	while (n > 0)
	{
		if (*p1 != *p2)
			return (*p1 - *p2);
		p1++;
		p2++;
		n--;
	}
	return (0);
}
/*
int main()
{
	unsigned char block1[] = {21, 22, 23, 24, 28};
	unsigned char block2[] = {21, 22, 23, 24, 25, 26};
	size_t n = sizeof(block1);

	int result = ft_memcmp(block1, block2, n);

	if (result < 0)
	{
		printf("block1 < block2.\n");
	}
	else if (result > 0)
	{
		printf("block1 > block2.\n");
	}
	else
	{
		printf("block1 = block2.\n");
	}
	return (0);
}
*/
//Se utiliza para comparar los n primeros bytes de dos bloques de memoria

/*
int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*p1; // Puntero a unsigned char para recorrer la memoria s1
	unsigned char	*p2; // Puntero a unsigned char para recorrer la memoria s2

	El tipo char puede ser tanto con signo (signed) como sin signo (unsigned), 
	dependiendo de la implementación del compilador. Si char es con signo, los 
	valores mayores a 127 se interpretan como negativos, lo que puede llevar a 
	comparaciones incorrectas. Usar unsigned char asegura que todos los valores 
	posibles de un byte (0-255) se traten como números positivos. Esto evita 
	los problemas que podrían surgir si los bytes tienen valores mayores a 127,
	garantizando comparaciones correctas y consistentes.

	p1 = (unsigned char *)s1; // Convertir el puntero s1 a unsigned char
	p2 = (unsigned char *)s2; // Convertir el puntero s2 a unsigned char

	Dado que s1 y s2 son punteros genéricos (void*), es necesario convertirlos
	a un tipo específico para acceder a los datos que apuntan. unsigned char* 
	es apropiado porque permite acceder a los datos byte a byte sin problemas 
	de signo
	
	// Si n es 0, las memorias son iguales, así que devolvemos 0
	if (n == 0)
		return (0);
	
	// Recorremos las memorias comparando byte a byte hasta que n sea 0
	while (n > 0)
	{
		if (*p1 != *p2)  // Si encontramos una diferencia en los bytes
			return (*p1 - *p2); // Devuelve la diferencia entre los bytes
		p1++;
		p2++;
		n--;
	}
	return (0); // si llega aqui las memorias son iguales
}
*/

/* Ejemplo
Supongamos que tenemos dos bloques de memoria s1 y s2 que contienen los 
siguientes valores:

c
Copy code
unsigned char s1[] = {0x12, 0x34, 0x56, 0x78, 0x9A};
unsigned char s2[] = {0x12, 0x34, 0x56, 0x78, 0xFF};
size_t n = 5;
Queremos comparar estos dos bloques de memoria byte a byte.

Llamada a la función
c
Copy code
int result = ft_memcmp(s1, s2, n);
Código de la función
c
Copy code
int ft_memcmp(const void *s1, const void *s2, size_t n)
{
    unsigned char *p1;
    unsigned char *p2;

    p1 = (unsigned char *)s1;
    p2 = (unsigned char *)s2;
    if (n == 0)
        return (0);
    while (n > 0)
    {
        if (*p1 != *p2)
            return (*p1 - *p2);
        p1++;
        p2++;
        n--;
    }
    return (0);
}
Paso a paso
Declaración y asignación de punteros:

c
Copy code
unsigned char *p1;
unsigned char *p2;

p1 = (unsigned char *)s1;  // p1 apunta al inicio de s1
p2 = (unsigned char *)s2;  // p2 apunta al inicio de s2
Verificación del tamaño n:

c
Copy code
if (n == 0)
    return (0);
n no es 0, así que continuamos.

Bucle de comparación byte a byte:

c
Copy code
while (n > 0)
{
    if (*p1 != *p2)
        return (*p1 - *p2);
    p1++;
    p2++;
    n--;
}
Iteraciones del bucle:
Primera iteración:

n = 5
*p1 = 0x12, *p2 = 0x12
0x12 == 0x12 → No hay diferencia, continuar.
Incrementamos p1 y p2, decrementamos n.
Segunda iteración:

n = 4
*p1 = 0x34, *p2 = 0x34
0x34 == 0x34 → No hay diferencia, continuar.
Incrementamos p1 y p2, decrementamos n.
Tercera iteración:

n = 3
*p1 = 0x56, *p2 = 0x56
0x56 == 0x56 → No hay diferencia, continuar.
Incrementamos p1 y p2, decrementamos n.
Cuarta iteración:

n = 2
*p1 = 0x78, *p2 = 0x78
0x78 == 0x78 → No hay diferencia, continuar.
Incrementamos p1 y p2, decrementamos n.
Quinta iteración:

n = 1
*p1 = 0x9A, *p2 = 0xFF
0x9A != 0xFF → Diferencia encontrada.
La función retorna 0x9A - 0xFF = -101.
Retorno final
c
Copy code
return (0);  // Este punto no se alcanza debido a la diferencia encontrada.
Resultado
El valor de result será -101, indicando que los bloques de memoria difieren en el
 quinto byte.

Estado final
c
Copy code
// p1 apunta a después del último byte comparado en s1.
// p2 apunta a después del último byte comparado en s2.
// n es 0 después de la última iteración.
Este paso a paso demuestra cómo la función ft_memcmp compara byte a byte dos 
bloques de memoria y retorna la diferencia en el primer byte donde encuentra una 
discrepancia. */