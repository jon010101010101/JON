/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/09 11:28:49 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/23 18:34:12 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlen(const char *str)
{
	int	count;

	count = 0;
	while (*str != '\0')
	{
		count++;
		str++;
	}
	return (count);
}
/*
int main() 
{
    char cadena[] = "Cuéntameeeeee esto!";
    int length = ft_strlen(cadena);
    printf("La longitud de la cadena es: %d\n", length);
    
    return 0;
}
*/
// Calcula la longitud de una cadena.
// str: Puntero a la cadena de caracteres.
// Devuelve: El número de caracteres en la cadena, excluyendo el carácter nulo
// final.

/*
size_t	ft_strlen(const char *str)
{
	int	count;		// Contador para la longitud de la cadena.

	count = 0;
	while (*str != '\0')	// Recorrer la cadena hasta el carácter nulo final.
	{
		count++;		// Incrementar el contador en cada iteración.
		str++;			// Avanzar al siguiente carácter.
	}
	return (count);		// Devolver la longitud de la cadena.
}
*/