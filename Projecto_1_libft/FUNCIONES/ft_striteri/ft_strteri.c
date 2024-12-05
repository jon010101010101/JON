/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strteri.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:53:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:33:32 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	
}
/* 
int	main(void)
{
	
}
 */
// DESCRIPCION. A cada carácter de la string ’s’, aplica la función
// ’f’ dando como parámetros el índice de cada carácter dentro de ’s’
// y la dirección del propio carácter, que podrá modificarse si es necesario.

// No devulve nada

// PARAMETROS. 
// s: La string que iterar.
// f: La función a aplicar sobre cada carácter.

// La función ft_striteri en C aplica una función f a cada carácter de la
// cadena s, pasando también el índice de ese carácter como primer argumento 
// a la función f.

/* // Función para aplicar una función a cada carácter de una cadena, pasando
 su índice como primer argumento //
void ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int i; // Variable para almacenar el índice actual

	i = 0; // Inicializamos el índice en 0

	// Verificamos si la cadena s o la función f son NULL
	if (s == NULL || f == NULL)
		return; // Si lo son, salimos de la función

	// Recorremos la cadena s hasta encontrar el carácter nulo '\0'
	while (s[i] != '\0')
	{
		f(i, &s[i]); // Llamamos a la función f con el índice actual y la 
		dirección del carácter actual de s como argumentos
		i++; // Incrementamos el índice para pasar al siguiente carácter de
		 s
	}
} */