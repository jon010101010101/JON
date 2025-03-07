/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:00:36 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/22 10:18:23 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t		i;
	const char	*ptr;

	i = 0;
	ptr = (const char *)s;
	while (i < n)
	{
		if (*ptr == (char)c)
		{
			return ((void *)ptr);
		}
		ptr++;
		i++;
	}
	return (NULL);
}

/* int main()
{
	char str[] = "Hello, Mary Ann!";
	char *ptr;

	ptr = ft_memchr(str, 'M', 15);

	if (ptr != NULL)
	{
		printf("Character found in position %ld.\n", ptr - str);
	}
	else
	{
		printf("Character not found in the first bytes.\n");
	}
	return (0);
} */
