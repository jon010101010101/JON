/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:57:49 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/21 10:26:58 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	size_t	i;
	char	*dst_ptr;
	char	*src_ptr;

	dst_ptr = (char *)dst;
	src_ptr = (char *)src;
	if (dst == src)
		return (dst);
	i = 0;
	while (i < n)
	{
		dst_ptr[i] = src_ptr[i];
		i++;
	}
	return (dst);
}
/*
int main()
{
	char src[] = "Hola, Manola!";
	char dst[20];

	ft_memcpy(dst, src, 15);

	printf("Después de ft_memcpy: %s\n", dst);

	return (0);
}
*/
// Copia un bloque de memoria desde src a dst, el n número de bytes

/*
void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	size_t	i;
	char	*dst_ptr;	// Puntero a char para recorrer el destino
	char	*src_ptr;	// Puntero a char constante para recorrer el origen

	dst_ptr = (char *)dst; // Convertir el puntero destino a char
	src_ptr = (char *)src;	// Convertir el puntero origen a char

	Los punteros void* son punteros genéricos que no tienen un tipo específico
	asociado, lo que impide el acceso directo a los datos que apuntan. Para 
	copiar bytes individuales, necesitamos un puntero de tipo específico.
	Convertimos void* a char* porque en C, un char tiene un tamaño de 1 byte. 
	Esto permite acceder y manipular los datos byte a byte.
	
// Si dst y src son iguales, no hay nada que copiar, así que devolvemos dst	
	if (dst == src)
		return (dst);
	i = 0;
	
// Copiamos byte a byte desde src a dst hasta que se copien n bytes	
	while (i < n)
	{
		dst_ptr[i] = src_ptr[i];   // Copiar el byte desde src a dst
		i++;
	}
	return (dst); // Devolvemos el puntero a dst
}
*/