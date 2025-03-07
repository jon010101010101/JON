/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 18:45:46 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/25 09:59:10 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t		src_len;
	size_t		i;

	i = 0;
	src_len = 0;
	if (!dst || !src)
		return (0);
	while (src[src_len] != '\0')
		src_len++;
	if (size == 0)
		return (src_len);
	while (i < size - 1 && src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (src_len);
}

/* int main(void)
{
	char dst1[20];
	char dst2[10];
	const char *src = "Hello, Maryann!";
	size_t result1, result2;
	size_t size1, size2;

	size1 = 20;
	result1 = ft_strlcpy(dst1, src, size1);

	printf("Long case:\n");
	printf("Source: %s\n", src);
	printf("Destination: %s\n", dst1);
	printf("Length of source: %zu\n", result1);

	size2 = 10;
	result2 = ft_strlcpy(dst2, src, size2);

	printf("Small case:\n");
	printf("Source: %s\n", src);
	printf("Destination: %s\n", dst2);
	printf("Length of source: %lu\n", ft_strlen(dst2));

	return (0);
} */
