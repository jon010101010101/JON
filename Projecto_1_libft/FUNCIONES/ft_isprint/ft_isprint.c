/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 10:54:12 by jurrutia          #+#    #+#             */
/*   Updated: 2024/04/19 17:15:41 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stddef.h>

int ft_isprint(int c)

{
	if (c >= 32 && c <= 126)
	{
		return (1);
	}
	return (0);
}

int main()
{
	char *n1 = "9";
	char *n2 = "A";
	char *n3 = "π";
	char *n4 = " ";
	int total1;
	int total2;
	int total3;
	int total4;

	total1 = ft_isprint(*n1);
	printf("Es imprimible?:%d\n", total1);
	total2 = ft_isprint(*n2);
	printf("Es imprimible?:%d\n", total2);
	total3 = ft_isprint(*n3);
	printf("Es imprimible?:%d\n", total3);
	total4 = ft_isprint(*n4);
	printf("Es imprimible?:%d\n", total4);

	return (0);
}

//Devuelve un valor distinto de cero si esta inlcuido en el intervalo 032-126 ASCII. es imprimible