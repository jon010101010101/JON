/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/04 19:32:57 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

// Función para cargar los recursos del juego (mapa, imágenes)
int	load_game_resources(t_game *game, char *map_file)
{
	if (load_map(game, map_file) < 0)
	{
		return (-1);
	}
	load_images(game);
	return (0);
}

// Función para crear la ventana y configurar hooks
int	setup_window_and_hooks(t_game *game)
{
	game->win = mlx_new_window(game->mlx, game->width * TILE_SIZE,
			game->height * TILE_SIZE, "So Long");
	if (!game->win)
	{
		fprintf(stderr, "Error: Could not create window\n");
		return (-1);
	}
	mlx_key_hook(game->win, key_press, game);
	mlx_hook(game->win, 17, 0, close_window,
		game);
	return (0);
}

int	main(int argc, char **argv)
{
	t_game	game;

	if (argc != 2)
	{
		fprintf(stderr, "Usage: %s <map_file>\n", argv[0]);
		return (1);
	}
	init_game(&game);
	if (load_game_resources(&game, argv[1]) < 0)
	{
		return (-1);
	}
	printf("Before rendering: Width = %d, Height = %d\n", game.width,
		game.height);
	if (setup_window_and_hooks(&game) < 0)
	{
		return (-1);
	}
	render_game(&game);
	mlx_loop(game.mlx);
	return (0);
}
