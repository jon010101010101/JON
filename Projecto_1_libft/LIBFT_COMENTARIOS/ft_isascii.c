/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 09:52:26 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/15 18:44:01 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isascii(int c)

{
	if (c >= 0 && c <= 127)
	{
		return (1);
	}
	return (0);
}

/*
int main()
{
	char *n1 = "9";
	char *n2 = "A";
	char *n3 = "π";
	int total1;
	int total2;
	int total3;

	total1 = ft_isascii(*n1);
	printf("Es ASCII?:%d\n", total1);
	total2 = ft_isascii(*n2);
	printf("Es ASCII?:%d\n", total2);
	total3 = ft_isascii(*n3);
	printf("Es ASCII?:%d\n", total3);

	return (0);
}
*/
//Devuelve un valor distinto de cero si esta inlcuido en el intervalo 0-127