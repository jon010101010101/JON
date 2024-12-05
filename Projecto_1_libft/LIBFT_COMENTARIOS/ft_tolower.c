/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 12:14:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/15 18:13:19 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_tolower(int c)

{
	if ((c >= 'A' && c <= 'Z'))
	{
		return (c + 32);
	}
	else
	{
		return (c);
	}
}
/*
int main()
{
	char letra1= 'H';
	char letra2= 'a';
	char letra3 = ' ';
	int letra_min1 = ft_tolower(letra1);
	int letra_min2 = ft_tolower(letra2);
	int letra_min3 = ft_tolower(letra3);
	
	printf("Si es mayúscula y cambia a minuscula?:%c\n", (char)letra_min1);
	printf("Si es mayúscula y cambia a minuscula?:%c\n", (char)letra_min2);
	printf("Si es mayúscula y cambia a minuscula?:%c\n", (char)letra_min3);

	return 0;
}
*/
// Convierte una letra mayúscula en minúscula