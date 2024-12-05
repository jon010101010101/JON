/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/20 10:48:13 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:34:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	
}
/*
int main(void)
{
	
}
*/

//DESCRIPCION. Elimina todos los caracteres de la string ’set’ 
//desde el principio y desde el final de ’s1’, hasta encontrar 
// un caracter no perteneciente a ’set’. La string resultante
//se devuelve con una reserva de malloc(3)

// VALOR DEVUELTO. La string recortada. NULL si falla la reserva
// de memoria.

// PARAMETROS. 
// s1: La string que debe ser recortada.
// set: Los caracteres a eliminar de la string.

// La función ft_strtrim toma dos cadenas de caracteres (s1 y set)
// y devuelve una nueva cadena que es una copia de s1 con los 
// caracteres que aparecen en set eliminados del principio y del final
// de la cadena.

/*
// Función para extraer una subcadena de una cadena dada//
char *ft_substr(char const *s, unsigned int start, size_t len)
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
