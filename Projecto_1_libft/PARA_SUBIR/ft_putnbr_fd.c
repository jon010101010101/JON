/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 18:23:22 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/01 19:39:30 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <fcntl.h>

void	ft_putnbr_fd(int n, int fd)
{
	int	divider;

	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		ft_putchar_fd('-', fd);
		n = -n;
	}
	divider = 1;
	while (n / divider >= 10)
		divider *= 10;
	while (divider != 0)
	{
		ft_putchar_fd((n / divider) + '0', fd);
		n %= divider;
		divider /= 10;
	}
}

int	main(void)
{
	int	number;
	int	fd;

	number = 12345;
	fd = open("A", O_WRONLY);
	ft_putnbr_fd(number, fd);
	return (0);
}
