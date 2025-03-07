/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 10:37:19 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:25:36 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalnum(int c)
{
	if (((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
		|| (c >= '0' && c <= '9'))
	{
		return (1);
	}
	return (0);
}

/* int main(void)
{
	char *n1 = "9";
	char *n2 = "A";
	char *n3 = "π";
	int total1;
	int total2;
	int total3;

	total1 = ft_isalnum(*n1);
	printf("Is alpha or isdigit?:%d\n", total1);
	total2 = ft_isalnum(*n2);
	printf("Is alpha or isdigit?:%d\n", total2);
	total3 = ft_isalnum(*n3);
	printf("Is alpha or isdigit?:%d\n", total3);

	return (0);
}
 */