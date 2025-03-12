/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   render_game.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 19:22:42 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>

// Clear the window and draw a tile
void	clear_and_draw_tile(t_game *game, int x, int y)
{
	void	*img;
	int		x_pixels;
	int		y_pixels;

	img = NULL;
	if (game->map[y][x] == '1')
		img = game->img_wall;
	else if (game->map[y][x] == '0')
		img = game->img_empty;
	else if (game->map[y][x] == 'C')
		img = game->img_collectible;
	else if (game->map[y][x] == 'E')
		img = game->img_exit;
	else if (game->map[y][x] == 'P')
	{
		img = game->img_player;
	}
	if (!img)
		return ;
	x_pixels = x * TILE_SIZE;
	y_pixels = y * TILE_SIZE;
	mlx_put_image_to_window(game->mlx, game->win, img, x_pixels, y_pixels);
}

// Draw the map
void	draw_map(t_game *game)
{
	int	x;
	int	y;

	y = 0;
	while (y < game->height)
	{
		x = 0;
		while (x < game->width)
		{
			clear_and_draw_tile(game, x, y);
			x++;
		}
		y++;
	}
}

// Draw the player
void	draw_player(t_game *game)
{
	int		player_x_pixels;
	int		player_y_pixels;
	void	*img;

	img = game->img_player;
	player_x_pixels = game->player_x * TILE_SIZE;
	player_y_pixels = game->player_y * TILE_SIZE;
	mlx_put_image_to_window(game->mlx, game->win, img,
		player_x_pixels, player_y_pixels);
}

// Display the number of moves
void	show_moves(t_game *game)
{
	char	*moves_str;
	char	*message;

	moves_str = ft_itoa(game->moves);
	message = ft_strjoin("Moves: ", moves_str);
	mlx_string_put(game->mlx, game->win, 10, 20, 0x00FFFFFF, message);
	free(moves_str);
	free(message);
}

// Render the game
int	render_game(t_game *game)
{
	if (!game)
		return (1);
	mlx_clear_window(game->mlx, game->win);
	draw_map(game);
	draw_player(game);
	show_moves(game);
	return (0);
}
