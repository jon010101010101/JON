/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strteri.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:53:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/11 11:37:01 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	i = 0;
	if (s == NULL || f == NULL)
		return ;
	while (s[i] != '\0')
	{
		f(i, &s[i]);
		i++;
	}
}
/* 
int	main(void)
{
	char			*s;
	char			*n_str;
	unsigned int	*funcion;

	s = "A ver si funciona";
	ft_striteri(n_str, funcion)
	printf("la cadena creada tras f es: %s\n", n_str);
	return (0);
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