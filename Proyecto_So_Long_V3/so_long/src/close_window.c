/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   close_window.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/04 19:05:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

// Función auxiliar para destruir las imágenes (parte 1)
static void	destroy_images_part1(t_game *game)
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

// Función auxiliar para destruir las imágenes (parte 2)
static void	destroy_images_part2(t_game *game)
{
	if (game->mlx)
	{
		if (game->img_exit)
			mlx_destroy_image(game->mlx, game->img_exit);
		if (game->img_player)
			mlx_destroy_image(game->mlx, game->img_player);
	}
}

// Función auxiliar para destruir la ventana y el display
static void	destroy_window_and_display(t_game *game)
{
	if (game->mlx)
	{
		if (game->win)
			mlx_destroy_window(game->mlx, game->win);
		mlx_destroy_display(game->mlx);
		free(game->mlx);
	}
}

int	close_window(void *param)
{
	t_game	*game;

	game = (t_game *)param;
	if (game)
	{
		destroy_images_part1(game);
		destroy_images_part2(game);
		destroy_window_and_display(game);
	}
	exit(0);
	return (0);
}
