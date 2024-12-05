/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 16:06:56 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/17 17:52:34 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *b, int c, size_t len)
{
	unsigned char	*ptr;
	unsigned char	value;
	unsigned char	*end;

	ptr = b;
	value = (unsigned char)c;
	end = ptr + len;
	while (ptr < end)
	{
		*ptr = value;
		ptr++;
	}
	return (b);
}

/* int main()
{
	char str[20];

	ft_memset(str, 'A', 20);

	printf("After ft_memset: %.*s\n", (int)sizeof(str), str);

	return (0);
} */
