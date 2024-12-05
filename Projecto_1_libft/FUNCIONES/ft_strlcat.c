/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/08 13:14:25 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:08:41 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	dstlen;
	size_t	srclen;
	size_t	total_len;
	size_t	i;

	dstlen = 0;
	srclen = 0;
	i = 0;
	while (dstlen < size && dst[dstlen] != '\0')
		dstlen++;
	while (src[srclen] != '\0')
		srclen++;
	total_len = dstlen + srclen;
	if (dstlen >= size)
		return (size + srclen);
	while (src[i] != '\0' && dstlen + i < size - 1)
	{
		dst[dstlen + i] = src[i];
		i++;
	}
	dst[dstlen + i] = '\0';
	return (total_len);
}
/*
int main()
{
	char dest[50] = "¡Hello good Morning!";
	char src[] = "String that will add";
	
	printf("Original string: %s\n", dest);
	printf("String to add: %s\n", src);

	size_t len = ft_strlcat(dest, src, sizeof(dest));

	printf("Added string: %s\n", dest);
	printf("Added string length: %zu\n", len);

	return 0;
}
*/