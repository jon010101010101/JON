/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 12:14:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/17 19:15:03 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

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

	return (0);
}

// Convierte una letra mayúscula en minúscula