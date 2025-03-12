/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_game.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 18:27:51 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "so_long.h"

void	init_game(t_game *game)
{
	init_mlx_and_map(game);
	init_player_and_images(game);
	create_window(game);
}

void	init_mlx_and_map(t_game *game)
{
	game->mlx = mlx_init();
	if (!game->mlx)
	{
		ft_putstr_fd("Error: Could not initialize MLX\n", 2);
		close_game(game);
		exit(1);
	}
	game->win = NULL;
	game->map = NULL;
	game->width = 0;
	game->height = 0;
}

void	init_player_and_images(t_game *game)
{
	game->player_x = 0;
	game->player_y = 0;
	game->exit_x = 0;
	game->exit_y = 0;
	game->collectibles = 0;
	game->collected = 0;
	init_game_values(game);
}

void	init_game_values(t_game *game)
{
	game->exit_count = 0;
	game->moves = 0;
	game->win_condition = 0;
	game->img_wall = NULL;
	game->img_empty = NULL;
	game->img_collectible = NULL;
	game->img_exit = NULL;
	game->img_player = NULL;
}

void	create_window(t_game *game)
{
	if (game->mlx && game->width > 0 && game->height > 0)
	{
		game->win = mlx_new_window(game->mlx, game->width * TILE_SIZE,
				game->height * TILE_SIZE, "So Long");
		if (!game->win)
		{
			ft_putstr_fd("Error: Could not create the window\n", 2);
			exit(1);
		}
	}
}
