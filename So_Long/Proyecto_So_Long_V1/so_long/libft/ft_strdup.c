/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 12:30:03 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/17 17:53:12 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *src)
{
	int		i;
	int		len;
	char	*dst;

	i = 0;
	len = 0;
	while (src[len] != '\0')
	{
		len++;
	}
	len++;
	dst = (char *)malloc(len * sizeof(char));
	if (dst == NULL)
		return (NULL);
	while (src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (dst);
}

/* int main()
{
	const char *original = "Hello, Mary Ann!";
	char *duplicate = strdup(original);

	if (duplicate != NULL)
	{
		printf("Original: %s\n", original);
		printf("duplicate: %s\n", duplicate);

		free(duplicate);
	}
	else
	{
		printf("Error: Could not duplicate string.\n");
	}
	return 0;
} */