/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/08 13:14:25 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/25 09:16:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	dstlen;
	size_t	srclen;
	size_t	total_len;
	size_t	i;

	dstlen = 0;
	srclen = 0;
	i = 0;
	while (dstlen < size && dst[dstlen] != '\0')
		dstlen++;
	while (src[srclen] != '\0')
		srclen++;
	total_len = dstlen + srclen;
	if (dstlen >= size)
		return (size + srclen);
	while (src[i] != '\0' && dstlen + i < size - 1)
	{
		dst[dstlen + i] = src[i];
		i++;
	}
	dst[dstlen + i] = '\0';
	return (total_len);
}

int	main(void)
{
	char	dst [20] = "Hello";
	const char *src = "Maryann!";
	size_t size;
	size_t result;

	size = 8;
	result = ft_strlcat(dst, src, size);
	printf("Result string with size: \"%s\", total lenght dst + src: %zu\n", dst, result);
	
	return (0);
}

// Devuelve el valor de la longitud de la cadena sumada

/*
size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	dstlen;     // Variable para almacenar la longitud
						// actual de la cadena de destino
	size_t	srclen;		// Variable para almacenar la longitud
						// de la cadena fuente
	size_t	total_len;	// Variable para almacenar la longitud
						// total después de la concatenación
	size_t	i;

	dstlen = 0;
	srclen = 0;
	i = 0;

// Calculamos la longitud actual de la cadena de destino
	while (dstlen < size && dst[dstlen] != '\0')
		dstlen++;

// Calculamos la longitud de la cadena fuente
	while (src[srclen] != '\0')
		srclen++;

// Calculamos la longitud total después de la concatenación
	total_len = dstlen + srclen;

// Si la longitud actual de la cadena de destino es mayor o igual que el
// tamaño dado, // devolvemos el tamaño dado más la longitud de la cadena fuente

	if (dstlen >= size)
		return (size + srclen);

// Copiamos los caracteres de la cadena fuente a la cadena de destino,
// asegurándonos de no exceder el tamaño dado
	while (src[i] != '\0' && dstlen + i < size - 1)
	{
		dst[dstlen + i] = src[i];
		i++;
	}
	dst[dstlen + i] = '\0'; 	// Añadimos el terminador nulo a la cadena
								//de destino

// Devolvemos la longitud total después de la concatenación
	return (total_len);
}
*/
