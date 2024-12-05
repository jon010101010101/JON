/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 18:45:46 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:11:26 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t dstsize)
{
	size_t		src_len;
	size_t		i;

	i = 0;
	src_len = 0;
	while (src[src_len] != '\0')
	{
		src_len++;
	}
	if (dstsize == 0)
	{
		return (src_len);
	}
	while (i < dstsize - 1 && src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (src_len);
}
/*
int main()
{
	char src[] = "¡Hello good Morning!";
	char dest[50] = "String is going to crush";
	size_t length = 5;

	size_t len = ft_strlcpy(dest, src, length);

	printf("Original string: %s\n", src);
	printf("copied string: %s\n", dest);
	printf("initial string length: %zu\n", len);
	printf("length of copied string: %zu\n", length);

	return (0);
}
*/