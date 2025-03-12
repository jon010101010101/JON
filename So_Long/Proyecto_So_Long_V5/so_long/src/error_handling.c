/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   error_handling.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/04 16:38:02 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>

int	handle_error(const char *message, int fd)
{
	ft_putstr_fd("Error: ", 2);
	ft_putstr_fd((char *)message, 2);
	ft_putstr_fd("\n", 2);
	if (fd != -1)
		close(fd);
	return (-1);
}
