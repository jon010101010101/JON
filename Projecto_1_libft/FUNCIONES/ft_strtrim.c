/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/20 10:48:13 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:23:37 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	int		len;
	int		start;
	int		end;
	int		result_len;
	char	*result;

	len = ft_strlen(s1);
	start = 0;
	end = len - 1;
	while (s1[start] != '\0' && ft_strchr(set, s1[start]) != NULL)
		start++;
	while (s1[start] != '\0' && ft_strchr(set, s1[end]) != NULL)
		end--;
	result_len = end - start + 1;
	result = (char *)malloc((result_len + 1) * sizeof(char));
	if (result == NULL)
		return (NULL);
	if (result != NULL)
		ft_strlcpy(result, s1 + start, result_len + 1);
	result[result_len] = '\0';
	return (result);
}
/*
int main(void)
{
	char	*s1;
	char	*set;

	s1 = "Hello, Maryann";
	set = "ry";

	printf("The resulting string is: %s\n", ft_strtrim(s1,set));
	return (0);
}
*/