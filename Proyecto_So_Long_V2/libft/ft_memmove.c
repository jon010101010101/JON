/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 18:46:08 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 19:36:34 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	size_t		i;
	char		*dst_ptr;
	const char	*src_ptr;

	dst_ptr = (char *)dst;
	src_ptr = (const char *)src;
	if (src == NULL && dst == NULL)
		return (NULL);
	if (dst_ptr < src_ptr || dst_ptr >= src_ptr + len)
		ft_memcpy (dst, src, len);
	else
	{
		i = len;
		while (i > 0)
		{
			dst_ptr[i - 1] = src_ptr[i - 1];
			i--;
		}
	}
	return (dst);
}

/* int main(void)
{
	char str[] = "Helo, Mary Ann!";
	ft_memmove(str + 4, "1234", 3);

	printf("After ft_memmove: %s\n", str);

	return (0);
} */
