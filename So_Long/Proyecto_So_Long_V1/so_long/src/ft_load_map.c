/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_load_map.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:49:30 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_load_map.h"
#include "so_long.h"
#include "ft_error.h"
#include "ft_map_utils.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>

int	process_line(t_game *game, char *buffer, int line_length)
{
	int	i; // Declaración al principio del bloque

	game->map[game->height] = ft_strdup(buffer);
	if (!game->map[game->height])
		return (0);
	i = 0; // Asignación en línea separada
	while (i < line_length)
	{
		if (buffer[i] == 'E')
			game->exit_count++;
		else if (buffer[i] == 'C')
			game->collectibles++;
		else if (buffer[i] == 'P')
		{
			game->player_x = i;
			game->player_y = game->height;
		}
		i++;
	}
	return (1);
}

int	read_map_file(t_game *game, int fd)
{
	char	buffer[MAX_MAP_WIDTH + 1];
	ssize_t	read_bytes;
	char	*newline;
	int		line_length;

	while ((read_bytes = read(fd, buffer, MAX_MAP_WIDTH)) > 0)
	{
		buffer[read_bytes] = '\0';
		newline = ft_strchr(buffer, '\n');
		if (newline)
			*newline = '\0';
		line_length = ft_strlen(buffer);
		if (game->width == 0)
			game->width = line_length;
		else if (line_length != game->width)
			return (0);
		if (!process_line(game, buffer, line_length))
			return (0);
		game->height++;
		if (game->height >= MAX_MAP_HEIGHT)
			return (0);
		if (newline)
		{
			ssize_t offset; // Declarar offset antes de usarlo

			offset = read_bytes - (newline - buffer + 1); // Asignación separada
			lseek(fd, -offset, SEEK_CUR);
		}
	}
	return (1);
}

int	validate_and_print(t_game *game)
{
	if (!validate_map(game))
	{
		handle_error("Invalid map configuration\n", game, -1);
		return (0);
	}
	ft_printf("Map loaded: Width = %d, Height = %d, Exits = %d, ",
		game->width, game->height, game->exit_count);
	ft_printf("Collectibles = %d\n", game->collectibles);
	print_map(game);
	return (0);
}

int	load_map(t_game *game, const char *filename)
{
	int	fd;

	fd = open(filename, O_RDONLY);
	if (fd == -1)
		handle_error("Could not open map file\n", game, fd);
	game->map = ft_calloc(MAX_MAP_HEIGHT, sizeof(char *));
	if (!game->map)
		handle_error("Could not allocate memory for the map\n", game, fd);
	game->height = 0;
	game->width = 0;
	game->exit_count = 0;
	game->collectibles = 0;
	if (!read_map_file(game, fd))
		handle_error("Error reading map file\n", game, fd);
	close(fd);
	return (validate_and_print(game));
}
