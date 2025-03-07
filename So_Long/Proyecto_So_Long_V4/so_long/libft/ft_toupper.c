/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_toupper.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 13:13:05 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 19:34:05 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_toupper(int c)

{
	if ((c >= 'a' && c <= 'z'))
	{
		return (c - 32);
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
	int letter_min1 = ft_toupper(letter1);
	int letter_min2 = ft_toupper(letter2);
	int letter_min3 = ft_toupper(letter3);

	printf("If it is lowercase it changes to uppercase?:%c\n", 
	(char)letter_min1);
	printf("If it is lowercase it changes to uppercase?:%c\n", 
	(char)letter_min2);
	printf("If it is lowercase it changes to uppercase?:%c\n", 
	(char)letter_min3);

	return (0);
}
*/