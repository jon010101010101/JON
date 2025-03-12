/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   map_utils.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 19:20:02 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <unistd.h>

// Handle file lseek
int	handle_lseek(int fd, ssize_t read_bytes, char *buffer)
{
	char	*newline_ptr;
	off_t	offset;

	newline_ptr = ft_strchr(buffer, '\n');
	offset = -(read_bytes - (newline_ptr - buffer + 1));
	lseek(fd, offset, SEEK_CUR);
	return (0);
}
