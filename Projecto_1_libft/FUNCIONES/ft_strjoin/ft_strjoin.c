/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:33:52 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:33:43 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	
}
/*

int	main(void)
{
	
}
*/
// Este código implementa la función ft_strjoin, que concatena dos cadenas
// (s1 y s2) y devuelve una nueva cadena resultante. 

// DESCRIPCION. Reserva (con malloc(3)) y devuelve una nueva string, 
//formada por la concatenación de ’s1’ y ’s2’.

// VALOR DEVUELTO. La nueva string. NULL si falla la reserva de memoria.

// PARAMETROS. 
// s1: La primera string.
// s2: La string a añadir a ’s1’.

// La función ft_strjoin en C concatena dos cadenas de caracteres s1 y s2
// y devuelve una nueva cadena que contiene la concatenación de ambas.

/* 
//Función para concatenar dos cadenas //
char *ft_strjoin(char const *s1, char const *s2)
{
	int count1;     // Variable para almacenar la longitud de la primera 
					cadena s1
	int count2;     // Variable para almacenar la longitud de la segunda 
					cadena s2
	char *str;      // Puntero para almacenar la cadena resultante

	// Calculamos la longitud de la primera cadena s1
	count1 = ft_strlen(s1);

	// Calculamos la longitud de la segunda cadena s2
	count2 = ft_strlen(s2);

	// Asignamos memoria para la cadena resultante, más uno adicional para 
	el carácter nulo '\0'
	str = malloc(count1 + count2 + 1);

	// Verificamos si la asignación de memoria fue exitosa
	if (str == NULL)
		return (NULL); // Si falla, devolvemos NULL

	// Copiamos la primera cadena s1 en la cadena resultante
	ft_strlcpy(str, s1, count1 + 1);

	// Concatenamos la segunda cadena s2 a la cadena resultante
	ft_strlcat(str, s2, count1 + count2 + 1);

	// Devolvemos la cadena resultante
	return (str);
} */