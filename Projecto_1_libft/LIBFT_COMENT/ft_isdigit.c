/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/09 13:16:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/11 12:34:16 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isdigit(int c)

{
	if (c >= '0' && c <= '9')
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

	total1 = ft_isdigit(*n1);
	printf("Es Dígito?:%d\n", total1);
	total2 = ft_isdigit(*n2);
	printf("Es Dígito?:%d\n", total2);
	total3 = ft_isdigit(*n3);
	printf("Es Dígito?:%d\n", total3);

	return (0);
}
*/
// Devuelve un valor distinto de cero si esta inlcuido en el intervalo 0-9