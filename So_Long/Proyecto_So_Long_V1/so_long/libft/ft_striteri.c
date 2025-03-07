/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:53:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/17 16:42:45 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	i = 0;
	if (s == NULL)
		return ;
	while (s[i] != '\0')
	{
		f(i, &s[i]);
		i++;
	}
}
/* 
void example_function(unsigned int i, char *s)
{
		(void) i;
		if (*s >= 'a' && *s <= 'z')
			*s -= 32;
}

int	main(void)
{
	char	s[] = "Let's see if it works";
	ft_striteri(s, &example_function);
	printf("the string created after f is: %s\n", s);
	return (0);
} */
