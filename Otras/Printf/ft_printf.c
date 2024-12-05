/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/10 08:53:29 by josantia          #+#    #+#             */
/*   Updated: 2024/05/28 21:34:57 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *str, ...)
{
	int		i;
	int		size;
	va_list	argument;

	i = 0;
	size = 0;
	va_start(argument, str);
	while (str[i] != '\0')
	{
		if (str[i] == '%')
		{
			i++;
			size += ft_printf_format(argument, str[i]);
		}
		else
		{
			size += ft_printf_character(str[i]);
		}
		i++;
	}
	va_end(argument);
	return (size);
}

int	ft_printf_format(va_list argument, const char c)
{
	int	size;

	size = 0;
	if (c == 'c')
		size += ft_printf_character(va_arg(argument, int));
	else if (c == 's')
		size += ft_printf_string(va_arg(argument, char *));
	else if (c == 'i' || c == 'd')
		size += ft_printf_int(va_arg(argument, int));
	else if (c == 'x' || c == 'X')
		size += ft_printf_hexa(va_arg(argument, int), c);
	else if (c == 'u')
		size += ft_printf_unsigned(va_arg(argument, unsigned int));
	else if (c == 'p')
		size += ft_printf_pointer(va_arg(argument, unsigned long long));
	else
		size += ft_printf_character(c);
	return (size);
}
