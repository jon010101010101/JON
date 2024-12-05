/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:57:49 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:54:21 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dst, const void *src, size_t n)
{
	size_t	i;
	char	*dst_ptr;
	char	*src_ptr;

	dst_ptr = (char *)dst;
	src_ptr = (char *)src;
	if (dst == src)
		return (dst);
	i = 0;
	while (i < n)
	{
		dst_ptr[i] = src_ptr[i];
		i++;
	}
	return (dst);
}
/* 
int main()
{
	char src[] = "Hello, Mary Ann!";
	char dst[20];

	ft_memcpy(dst, src, 10);

	printf("After ft_memcpy: %s\n", dst);

	return (0);
} */
