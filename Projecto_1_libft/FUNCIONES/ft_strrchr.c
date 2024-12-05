/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:46:55 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:21:29 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*ptr;

	i = 0;
	ptr = 0;
	while (s[i])
	{
		if (s[i] == (char)c)
			ptr = (char *)(s + i);
		i++;
	}
	if (s[i] == (char)c)
		ptr = (char *)(s + i);
	return (ptr);
}

/*
int main(void)
{
	const char string[] = "Hello, Mary Ann!";
	int character = 'o';

	char *result = ft_strrchr(string, character);

	if (result != NULL)
	{
	printf("The last \"%c\" found is: %s\n", character, result);
	} 
	else
	{
	printf("The character \"%c\" was not found in the string.\n", character);
	}
	return (0);
}
*/