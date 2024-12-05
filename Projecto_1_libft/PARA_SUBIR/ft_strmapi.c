/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/20 11:40:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/01 19:42:26 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*n_str;
	int		i;
	int		size_str;

	if (s == NULL)
		return (NULL);
	size_str = ft_strlen(s);
	n_str = (char *) malloc ((size_str +1) * sizeof(char));
	if (n_str == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0')
	{
		n_str[i] = f(i, s[i]);
		i++;
	}
	n_str[i] = '\0';
	return (n_str);
}

char ft_example_function(unsigned int i, char c)
{
		(void) i;
		if (c >= 'a' && c <= 'z')
			return (c -= 32);
		return (c);
}

int	main(void)
{
	char			*s;
	char			*n_str;
	
	s = "abcdefg";
	n_str = ft_strmapi(s, ft_example_function);
	printf("the string created after f is: %s\n", n_str);
	free (n_str);
	return (0);
} 
