/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/08 13:00:16 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:54:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalpha(int c)
{
	if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
	{
		return (1);
	}
	return (0);
}

/* 
int main(void)
{
	char *n1 = "9";
	char *n2 = "A";
	char *n3 = "π";
	int total1;
	int total2;
	int total3;

	total1 = ft_isalpha(*n1);
	printf("Is Alpha?:%d\n", total1);
	total2 = ft_isalpha(*n2);
	printf("Is Alpha?:%d\n", total2);
	total3 = ft_isalpha(*n3);
	printf("Is Alpha?:%d\n", total3);
	
	return (0);
} 
*/
