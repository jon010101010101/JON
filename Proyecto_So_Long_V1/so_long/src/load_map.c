/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   load_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:50:32 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

void	free_map(t_game *game)
{
	int	i;

	i = 0;
	while (i < game->height)
	{
		if (game->map[i])
			free(game->map[i]);
		i++;
	}
	free(game->map);
}

void	handle_error(char *message, t_game *game, int fd)
{
	ft_putstr_fd("Error\n", 2);
	ft_putstr_fd(message, 2);
	if (fd > 0)
		close(fd);
	if (game && game->map)
		free_map(game);
	if (game)
		free(game);
	exit(EXIT_FAILURE);
}

int	process_line(t_game *game, char *buffer, int line_length); // Prototipo

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
			lseek(fd, -(read_bytes - (newline - buffer + 1)), SEEK_CUR);
	}
	return (1);
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
	return (0);
}
