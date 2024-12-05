/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: josantia <josantia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/10 09:08:14 by josantia          #+#    #+#             */
/*   Updated: 2024/05/28 18:25:08 by josantia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include <unistd.h>

int	ft_printf(const char *str, ...);
int	ft_printf_format(va_list argument, const char c);
int	ft_printf_character(char c);
int	ft_printf_string(char *str);
int	ft_printf_int(int n);
int	ft_printf_unsigned(unsigned int n);
int	ft_printf_hexa(unsigned int n, char mayus);
int	ft_printf_pointer(unsigned long long ptr);