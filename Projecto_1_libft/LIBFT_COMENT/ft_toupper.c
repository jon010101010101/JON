/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 13:13:05 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/15 18:13:22 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_toupper(int c)

{
	if ((c >= 'a' && c <= 'z'))
	{
		return (c - 32);
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
	int letra_min1 = ft_toupper(letra1);
	int letra_min2 = ft_toupper(letra2);
	int letra_min3 = ft_toupper(letra3);

	printf("Si es minúscula cambia a mayúscula?:%c\n", (char)letra_min1);
	printf("Si es minúscula cambia a mayúscula?:%c\n", (char)letra_min2);
	printf("Si es minúscula cambia a mayúscula?:%c\n", (char)letra_min3);

	return 0;
}
*/
// Convierte una letra minúscula en mayúscula