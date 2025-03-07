/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   map_reader.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:27:36 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int	process_map_line(char *line_start, t_game *game, int total_height);

// Procesa el búfer leído del archivo
int	process_buffer(char *buffer, t_game *game, int *total_height)
{
	char	*line_start;
	char	*newline;

	line_start = buffer;
	while (1)
	{
		newline = ft_strchr(line_start, '\n');
		if (newline == NULL)
			break ;
		*newline = '\0';
		if (process_map_line(line_start, game, *total_height) == -1)
			return (-1);
		(*total_height)++;
		line_start = newline + 1;
	}
	if (*line_start != '\0')
	{
		if (process_map_line(line_start, game, *total_height) == -1)
			return (-1);
		(*total_height)++;
	}
	return (0);
}

// Lee el mapa desde el archivo
int	read_map_from_file(int fd, t_game *game)
{
	char	buffer[MAX_MAP_WIDTH + 1];
	ssize_t	read_bytes;
	int		total_height;

	total_height = 0;
	read_bytes = read(fd, buffer, MAX_MAP_WIDTH);
	if (read_bytes == -1)
		return (-1);
	while (read_bytes > 0)
	{
		buffer[read_bytes] = '\0';
		if (process_buffer(buffer, game, &total_height) == -1)
			return (-1);
		read_bytes = read(fd, buffer, MAX_MAP_WIDTH);
	}
	if (read_bytes == -1)
		return (-1);
	game->height = total_height;
	return (0);
}
