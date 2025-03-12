/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cleanup.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 19:17:05 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

// Auxiliary function to destroy images (part 1)
void	destroy_images_part1(t_game *game)
{
	if (game->mlx)
	{
		if (game->img_wall)
			mlx_destroy_image(game->mlx, game->img_wall);
		if (game->img_empty)
			mlx_destroy_image(game->mlx, game->img_empty);
		if (game->img_collectible)
			mlx_destroy_image(game->mlx, game->img_collectible);
	}
}

// Auxiliary function to destroy images (part 2)
void	destroy_images_part2(t_game *game)
{
	if (game->mlx)
	{
		if (game->img_exit)
			mlx_destroy_image(game->mlx, game->img_exit);
		if (game->img_player)
			mlx_destroy_image(game->mlx, game->img_player);
	}
}

// Auxiliary function to destroy the window and the display
void	destroy_window_and_display(t_game *game)
{
	if (game->mlx)
	{
		if (game->win)
			mlx_destroy_window(game->mlx, game->win);
		mlx_destroy_display(game->mlx);
		free(game->mlx);
	}
}
