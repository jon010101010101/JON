/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 12:14:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:34:20 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_tolower(int c)

{
	if ((c >= 'A' && c <= 'Z'))
	{
		return (c + 32);
	}
	else
	{
		return (c);
	}
}
/*
int main(void)
{
	char letter1= 'H';
	char letter2= 'a';
	char letter3 = ' ';
	int letter_min1 = ft_tolower(letter1);
	int letter_min2 = ft_tolower(letter2);
	int letter_min3 = ft_tolower(letter3);
	
	printf("If it is uppercase and changes to lowercase?:%c\n", 
	(char)letter_min1);
	printf("If it is uppercase and changes to lowercase?:%c\n", 
	(char)letter_min2);
	printf("If it is uppercase and changes to lowercase?:%c\n", 
	(char)letter_min3);

	return (0);
}
*/