/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/24 20:05:16 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/19 11:28:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
/* #include <string.h>
#include <stdio.h>
#include <stdlib.h> */

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*str;
	size_t	size_s;
	size_t	i;

	if (s == NULL)
		return (NULL);
	size_s = ft_strlen((char *)s);
	if (start >= size_s || len == 0)
		return (ft_strdup(""));
	if (start + len > size_s)
		len = size_s - start;
	str = malloc(len + 1);
	if (str == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0' && len > 0)
	{
		str[i] = s[start];
		start++;
		len--;
		i++;
	}
	str[i] = '\0';
	return (str);
}

/* int	main(void)
{
	char const				*s;
	unsigned int			start;
	size_t					len;

	s = "ABCDEFGH";
	start = 2;
	len = 3;
	printf("The substring is: %s\n", ft_substr(s, start, len));
	return (0);
} */
