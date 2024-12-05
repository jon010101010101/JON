/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/28 18:04:50 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/11 10:07:44 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strjoin(char *s1, char *s2)
{
	char	*str;
	size_t	i;
	size_t	c;

	if (!s1)
	{
		s1 = malloc(sizeof(char) + 1);
		if (!s1)
			return (0);
		s1[0] = 0;
	}
	str = (char *)malloc(sizeof(char) * ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!str)
		return (ft_free(&s1));
	i = -1;
	while (s1[++i])
		str[i] = s1[i];
	c = -1;
	while (s2[++c])
		str[i + c] = s2[c];
	str[i + c] = '\0';
	free(s1);
	return (str);
}

size_t	ft_strlen(char *str)
{
	int	count;

	count = 0;
	while (*str != '\0')
	{
		count++;
		str++;
	}
	return (count);
}

char	*ft_strchr(char *s, int c)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == (char)c)
			return ((char *)&s[i]);
		i++;
	}
	if (s[i] == (char)c)
		return ((char *)&s[i]);
	return (NULL);
}

char	*ft_substr(char *s, unsigned int start, size_t len)
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

char	*ft_strdup(char *src)
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
