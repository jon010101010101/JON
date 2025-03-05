/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   load_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:30:14 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int	read_map_from_file(int fd, t_game *game);
int	validate_map(t_game *game);

// Inicializa las variables del juego
void	init_game_variables(t_game *game)
{
	game->width = 0;
	game->height = 0;
	game->exit_count = 0;
	game->collectibles = 0;
}

// Allocates memory for the map
int	allocate_map_memory(t_game *game, int fd)
{
	game->map = ft_calloc(MAX_MAP_HEIGHT, sizeof(char *));
	if (!game->map)
	{
		close(fd);
		return ((handle_error("Could not allocate memory", -1)));
	}
	return (0);
}

// Function to open the map file
int	open_map_file(const char *filename)
{
	int	fd;

	fd = open(filename, O_RDONLY);
	if (fd == -1)
		return (handle_error("Could not open map file", -1));
	return (fd);
}

// Function to load map data and validate
int	load_and_validate_map(int fd, t_game *game)
{
	if (read_map_from_file(fd, game) == -1)
	{
		close(fd);
		return (-1);
	}
	if (!validate_map(game))
	{
		close(fd);
		return (-1);
	}
	return (0);
}

// Carga el mapa desde el archivo
int	load_map(t_game *game, const char *filename)
{
	int	fd;

	fd = open_map_file(filename);
	if (fd == -1)
		return (-1);
	if (allocate_map_memory(game, fd) == -1)
		return (-1);
	init_game_variables(game);
	if (load_and_validate_map(fd, game) == -1)
		return (-1);
	close(fd);
	printf("Initial player position -\n");
	printf("X: %d, Y: %d\n", game->player_x, game->player_y);
	return (0);
}
