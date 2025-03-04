/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 11:25:36 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 19:07:52 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
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

/* int main()
{
	const char string[] = "Hello, Mary Ann!";
	char character = 'a';

	char *result = ft_strchr(string, character);

	if (result != NULL)
	{
	printf("The first \"%c\" found is: %s\n", character, result);
	} 
	else
	{
	printf("The character \"%c\" was not found in the string. %s\n", character,
	 result);
	}
	return 0;
} */
