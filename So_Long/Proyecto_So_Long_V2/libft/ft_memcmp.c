/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 18:17:01 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:31:48 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	unsigned char	*p1;
	unsigned char	*p2;

	p1 = (unsigned char *)s1;
	p2 = (unsigned char *)s2;
	if (n == 0)
		return (0);
	while (n > 0)
	{
		if (*p1 != *p2)
			return (*p1 - *p2);
		p1++;
		p2++;
		n--;
	}
	return (0);
}
/* 
int main(void)
{
	unsigned char block1[] = {21, 22, 23, 24, 28};
	unsigned char block2[] = {21, 22, 23, 24, 25, 26};
	size_t n = sizeof(block1);

	int result = ft_memcmp(block1, block2, n);

	if (result < 0)
	{
		printf("block1 < block2.\n");
	}
	else if (result > 0)
	{
		printf("block1 > block2.\n");
	}
	else
	{
		printf("block1 = block2.\n");
	}
	return (0);
}
 */
