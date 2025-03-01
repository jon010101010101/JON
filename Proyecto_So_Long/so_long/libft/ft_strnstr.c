/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 11:27:38 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/21 19:12:31 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	little_len;
	size_t	i;

	if (*little == '\0')
		return ((char *) big);
	little_len = 0;
	while (little[little_len] != '\0')
		little_len++;
	while (*big != '\0' && len >= little_len)
	{
		i = 0;
		while (little[i] != '\0' && big[i] == little[i])
			i++;
		if (little[i] == '\0')
			return ((char *) big);
		big++;
		len--;
	}
	return (NULL);
}

/* int main(void)
{
	const char *big = "Hello, Mary Ann!";
	const char *little = "Mary Ann";
	size_t len = 18;

	char *result = ft_strnstr(big, little, len);

	if (result != NULL)
	{
		printf("Substring found '%s' en '%s'\n", little, big);
		printf("The substring starts at position %ld\n", result - big);
	}
	else
	{
		printf("Substring not found '%s' en '%s'\n", little, big);
	}
	return (0);
} */
