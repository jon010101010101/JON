/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/08 13:11:45 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:16:57 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	while (n > 0 && *s1 != '\0' && *s2 != '\0')
	{
		if (*s1 != *s2)
		{
			return ((unsigned char)*s1 - (unsigned char)*s2);
		}
		s1++;
		s2++;
		n--;
	}
	if (n == 0)
	{
		return (0);
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}
/*
int main(VOID)
{
	char str1[] = "JON";
	char str2[] = "JONIAMNOTJON";

	printf("Comparing '%s' y '%s': %d\n", str1, str2, 
	ft_strncmp(str1, str2, 4));

	return (0);
}
*/