/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 11:27:38 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:18:38 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	needle_len;
	size_t	i;

	if (*needle == '\0')
		return ((char *) haystack);
	needle_len = 0;
	while (needle[needle_len] != '\0')
		needle_len++;
	while (*haystack != '\0' && len >= needle_len)
	{
		i = 0;
		while (needle[i] != '\0' && haystack[i] == needle[i])
			i++;
		if (needle[i] == '\0')
			return ((char *) haystack);
		haystack++;
		len--;
	}
	return (NULL);
}
/*
int main(void)
{
	const char *haystack = "Hello, Mary Ann!";
	const char *needle = "Mary Ann";
	size_t len = 18;

	char *result = ft_strnstr(haystack, needle, len);

	if (result != NULL)
	{
		printf("Substring found '%s' en '%s'\n", needle, haystack);
		printf("The substring starts at position %ld\n", result - haystack);
	}
	else
	{
		printf("Substring not found '%s' en '%s'\n", needle, haystack);
	}
	return (0);
}
*/