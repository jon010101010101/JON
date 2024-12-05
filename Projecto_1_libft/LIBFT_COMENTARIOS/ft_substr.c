/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/24 20:05:16 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/02 11:55:27 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
/* #include <string.h>
#include <stdio.h>
#include <stdlib.h> */

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*str;
	size_t	size_s;
	size_t	i;

	if (s == NULL)
		return (NULL);
	size_s = ft_strlen((char *)s);
	if (start >= size_s || len == 0)
		return (ft_strdup(""));
	if (start + len > size_s)
		len = size_s - start;
	str = malloc(len + 1);
	if (str == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0' && len > 0)
	{
		str[i] = s[start];
		start++;
		len--;
		i++;
	}
	str[i] = '\0';
	return (str);
}
/*
int	main(void)
{
	char const				*s;
	unsigned int			start;
	size_t					len;

	s = "ABCDEFGH";
	start = 2;
	len = 3;
	printf("La substring es: %s\n", ft_substr(s, start, len));
	return (0);
}
*/
// DESCRIPCION. Reserva (con malloc(3)) y devuelve una substring de 
// la string ’s’. La substring empieza desde el índice ’start’ y
// tiene una longitud máxima ’len’.

// VALOR DEVUELTO. La substring resultante. NULL si falla la reserva 
// de memoria.

// PARAMETROS. s: La string desde la que crear la substring.
// start: El índice del caracter en ’s’ desde el que empezar 
// la substring. 
// len: La longitud máxima de la substring.

/* char *ft_substr(char const *s, unsigned int start, size_t len)
{
	char *str;         // Puntero para almacenar la nueva subcadena
	size_t size_s;     // Variable para almacenar el tamaño de la cadena s
	size_t i;          // Variable de iteración

	// Verificamos si la cadena de entrada s es NULL
	if (s == NULL)
		return (NULL); // Si es NULL, devolvemos NULL

	// Calculamos el tamaño de la cadena s usando la función ft_strlen
	size_s = ft_strlen((char *)s);

	// Verificamos si el índice de inicio start está fuera de los límites de
	 s o si la longitud len es 0
	if (start >= size_s || len == 0)
		return (ft_strdup("")); // Si es así, devolvemos una cadena vacía

	// Ajustamos la longitud len si es necesario para asegurarnos de que no
	 sobrepase el tamaño de s desde start
	if (start + len > size_s)
		len = size_s - start;

	// Asignamos memoria para la nueva subcadena str, más uno adicional para
	 el carácter nulo '\0'
	str = malloc(len + 1);
	// Verificamos si la asignación de memoria fue exitosa
	if (str == NULL)
		return (NULL); // Si falla, devolvemos NULL

	i = 0; // Inicializamos el índice i a 0
	// Copiamos len caracteres desde la posición start de s a str
	while (s[i] != '\0' && len > 0)
	{
		str[i] = s[start]; // Copiamos el carácter actual de s a la nueva 
		subcadena
		start++;           // Incrementamos el índice start para avanzar en s
		len--;             // Decrementamos la longitud restante
		i++;               // Incrementamos el índice i para avanzar en str
	}
	str[i] = '\0'; // Establecemos el último carácter de la nueva subcadena 
	como '\0' para terminarla
	return (str);  // Devolvemos la nueva subcadena str
} */