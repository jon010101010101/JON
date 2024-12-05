/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/09 11:14:53 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/01 19:40:48 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putendl_fd(char *s, int fd)
{
	if (!s)
		return ;
	while (*s)
		write(fd, s++, 1);
	write(fd, "\n", 1);
}

int	main(void)
{
	char	*message;
	int		fd;

	message = "Hello, Mary Ann!";
	fd = open("A", O_WRONLY);
	ft_putendl_fd(message, fd);
	return (0);
}
