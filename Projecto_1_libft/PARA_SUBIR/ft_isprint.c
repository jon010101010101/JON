/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 10:54:12 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:54:36 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isprint(int c)
{
	if (c >= 32 && c <= 126)
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
	char *n4 = " ";
	int total1;
	int total2;
	int total3;
	int total4;

	total1 = ft_isprint(*n1);
	printf("is printable?:%d\n", total1);
	total2 = ft_isprint(*n2);
	printf("is printable?:%d\n", total2);
	total3 = ft_isprint(*n3);
	printf("is printable?:%d\n", total3);
	total4 = ft_isprint(*n4);
	printf("is printable?:%d\n", total4);

	return (0);
}
*/