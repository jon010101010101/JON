/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_basic.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josantia <josantia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/10 09:05:52 by josantia          #+#    #+#             */
/*   Updated: 2024/05/28 18:24:51 by josantia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf_character(char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_printf_string(char *str)
{
	int	i;
	int	size;

	i = 0;
	size = 0;
	if (str == 0)
		return (ft_printf_string("(null)"));
	while (str[i] != '\0')
	{
		size += ft_printf_character(str[i]);
		i++;
	}
	return (size);
}

int	ft_printf_int(int n)
{
	int		size;
	long	num;

	num = n;
	size = 0;
	if (n < 0)
	{
		size = ft_printf_character('-');
		num = -num;
	}
	size += ft_printf_unsigned((unsigned int)num);
	return (size);
}

int	ft_printf_unsigned(unsigned int n)
{
	int	size;

	size = 0;
	if (n == 0)
		size += ft_printf_character('0');
	else
	{
		if (n / 10 != 0)
			ft_printf_unsigned(n / 10);
		ft_printf_character((n % 10) + '0');
		while (n > 0)
		{
			n /= 10;
			size++;
		}
	}
	return (size);
}
