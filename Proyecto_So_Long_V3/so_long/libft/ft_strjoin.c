/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:33:52 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/18 12:32:40 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		count1;
	int		count2;
	char	*str;

	count1 = ft_strlen(s1);
	count2 = ft_strlen(s2);
	str = malloc(count1 + count2 +1);
	if (str == NULL)
		return (NULL);
	ft_strlcpy(str, s1, count1 + 1);
	ft_strlcat(str, s2, count1 + count2 + 1);
	return (str);
}

/* int	main(void)
{
	char	*a;
	char	*b;
	char	*c;

	a = "123";
	b = "456";
	c = ft_strjoin(a, b);

	printf("the result is %s\n", c);
	return (0);
} */
