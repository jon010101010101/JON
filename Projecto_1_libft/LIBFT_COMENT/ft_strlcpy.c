/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 18:45:46 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/25 09:58:28 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t		src_len;
	size_t		i;

	i = 0;
	src_len = 0;
	if (!dst || !src)
		return (0);
	while (src[src_len] != '\0')
		src_len++;
	if (size == 0)
		return (src_len);
	while (i < size - 1 && src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (src_len);
}
int main(void)
{
	char dst1[20];
	char dst2[10];
	const char *src = "Hello, Maryann!";
	size_t result1, result2;
	size_t size1, size2;

	size1 = 20;
	result1 = ft_strlcpy(dst1, src, size1);

	printf("Long case:\n");
	printf("Source: %s\n", src);
	printf("Destination: %s\n", dst1);
	printf("Length of source: %zu\n", result1);

	size2 = 10;
	result2 = ft_strlcpy(dst2, src, size2);

	printf("Small case:\n");
	printf("Source: %s\n", src);
	printf("Destination: %s\n", dst2);
	printf("Length of source: %lu\n", ft_strlen(dst2));

	return (0);
}

// copia de la cadena origen la longitud que se indica size_t

/*
size_t	ft_strlcpy(char *dest, const char *src, size_t dstsize)
{
	size_t		src_len;
	size_t		i;

	i = 0;
	src_len = 0;
	
// 	// Calcular la longitud de la cadena de origen src.
	while (src[src_len] != '\0')
	{
		src_len++;
	}
	
// // Si dstsize es 0, devolver la longitud de src.
	if (dstsize == 0)
	{
		return (src_len);
	}
	
// Copiar los caracteres desde src a dest hasta alcanzar 
// el tamaño máximo o encontrar el carácter nulo final.	
	while (i < dstsize - 1 && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';     // Agregar un carácter nulo final a dest después 
						// de la copia.
	return (src_len);	// Devolver la longitud de src.
}
Copia una cadena desde src a dest con un tamaño máximo especificado.
**
** dest: Puntero al buffer de destino donde se copiará la cadena.
** src: Puntero a la cadena de origen que se copiará.
** dstsize: Tamaño máximo del buffer de destino, incluyendo el 
	carácter nulo final.
**
** Devuelve: El tamaño de la cadena de origen, es decir, el número
	 de caracteres en src, excluyendo el carácter nulo.
**
** Detalles de implementación:
** - Se calcula la longitud de la cadena de origen src.
** - Si dstsize es 0, se devuelve la longitud de src.
** - Se copian los caracteres desde src a dest hasta que se alcanza
	 el tamaño máximo o se encuentra el carácter nulo final.
** - Se agrega un carácter nulo final a dest después de la copia.
** - Se devuelve la longitud de src.
**
** Nota: Esta función es similar a strlcpy de la biblioteca estándar de C.
*/

/* PASO A PASO
Inicialización:

dest = buffer de tamaño 20
src = "Hello, world!"
dstsize = 20
src_len = 0
i = 0
Verificación de punteros nulos:

Si dest o src son NULL, retornar 0.
En nuestro caso, ambos son válidos, así que continuamos.
Calcular la longitud de src:

Iteración 1:
src[src_len] = 'H', incrementar src_len (src_len = 1)
Iteración 2:
src[src_len] = 'e', incrementar src_len (src_len = 2)
Iteración 3:
src[src_len] = 'l', incrementar src_len (src_len = 3)
Iteración 4:
src[src_len] = 'l', incrementar src_len (src_len = 4)
Iteración 5:
src[src_len] = 'o', incrementar src_len (src_len = 5)
Iteración 6:
src[src_len] = ',', incrementar src_len (src_len = 6)
Iteración 7:
src[src_len] = ' ', incrementar src_len (src_len = 7)
Iteración 8:
src[src_len] = 'w', incrementar src_len (src_len = 8)
Iteración 9:
src[src_len] = 'o', incrementar src_len (src_len = 9)
Iteración 10:
src[src_len] = 'r', incrementar src_len (src_len = 10)
Iteración 11:
src[src_len] = 'l', incrementar src_len (src_len = 11)
Iteración 12:
src[src_len] = 'd', incrementar src_len (src_len = 12)
Iteración 13:
src[src_len] = '!', incrementar src_len (src_len = 13)
Iteración 14:
src[src_len] = '\0', terminamos de contar (src_len = 13)
Verificar dstsize:

Si dstsize es 0, retornar src_len (13 en nuestro caso).
En nuestro caso, dstsize = 20, así que continuamos.
Copiar caracteres de src a dest:

Iteración 1:
i = 0, dest[0] = src[0] = 'H', incrementar i (i = 1)
Iteración 2:
i = 1, dest[1] = src[1] = 'e', incrementar i (i = 2)
Iteración 3:
i = 2, dest[2] = src[2] = 'l', incrementar i (i = 3)
Iteración 4:
i = 3, dest[3] = src[3] = 'l', incrementar i (i = 4)
Iteración 5:
i = 4, dest[4] = src[4] = 'o', incrementar i (i = 5)
Iteración 6:
i = 5, dest[5] = src[5] = ',', incrementar i (i = 6)
Iteración 7:
i = 6, dest[6] = src[6] = ' ', incrementar i (i = 7)
Iteración 8:
i = 7, dest[7] = src[7] = 'w', incrementar i (i = 8)
Iteración 9:
i = 8, dest[8] = src[8] = 'o', incrementar i (i = 9)
Iteración 10:
i = 9, dest[9] = src[9] = 'r', incrementar i (i = 10)
Iteración 11:
i = 10, dest[10] = src[10] = 'l', incrementar i (i = 11)
Iteración 12:
i = 11, dest[11] = src[11] = 'd', incrementar i (i = 12)
Iteración 13:
i = 12, dest[12] = src[12] = '!', incrementar i (i = 13)
Finalizamos la copia ya que i = dstsize - 1 = 19 - 1 = 18 (pero no llegamos tan 
lejos porque src tiene longitud 13).
Asegurarse de que la cadena dest está terminada en nulo:

dest[i] = '\0' (en este caso, dest[13] = '\0')
Retornar la longitud de src:

Retornar src_len = 13.
Resultado
En nuestro ejemplo, result tendrá el valor 13 (la longitud de "Hello, world!") 
y dest contendrá "Hello, world!" con un carácter nulo al final.

 */