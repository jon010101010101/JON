/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_base.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josantia <josantia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/10 11:35:50 by josantia          #+#    #+#             */
/*   Updated: 2024/05/28 18:24:31 by josantia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf_hexa(unsigned int n, char mayus)
{
	int	size;

	size = 0;
	if (n >= 16)
	{
		size += ft_printf_hexa(n / 16, mayus);
		size += ft_printf_hexa(n % 16, mayus);
	}
	else
	{
		if (n < 10)
			size += ft_printf_character(n + '0');
		else
		{
			if (mayus == 'x')
				size += ft_printf_character(n + 'a' - 10);
			else if (mayus == 'X')
				size += ft_printf_character(n + 'A' - 10);
		}
	}
	return (size);
}
