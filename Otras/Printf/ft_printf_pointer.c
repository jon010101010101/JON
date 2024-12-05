/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_pointer.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/16 16:48:54 by josantia          #+#    #+#             */
/*   Updated: 2024/05/28 21:34:46 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_search_pointer(unsigned long long ptr)
{
	int size;

	size = 0;
	if (ptr >= 16)
	{
		size += ft_search_pointer(ptr / 16);
		size += ft_search_pointer(ptr % 16);
	}
	else
	{
		if (ptr < 10)
			size += ft_printf_character(ptr + '0');
		else
			size += ft_printf_character(ptr - 10 + 'a');
	}
	return (size);
}
/*
int	ft_length_pointer(unsigned long long ptr)
{
	int	len;

	len = 0;
	while (ptr > 0)
	{
		len++;
		ptr /= 16;
	}
	return (len);
}
*/
int	ft_printf_pointer(unsigned long long ptr)
{
	int	size;

	size = 0;
	if (ptr == 0)
		size += ft_printf_string("(nil)");
	else
	{
		size = ft_printf_string("0x");
		size += ft_search_pointer(ptr);
		//size += ft_length_pointer(ptr);
	}
	return (size);
}
