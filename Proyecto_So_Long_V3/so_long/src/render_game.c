/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   render_game.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/04 12:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 12:21:02 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>

#include "../include/so_long.h"
#include <stdio.h>

// Limpia la ventana y dibuja un tile
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
	if (!img)
		return ;
	x_pixels = x * TILE_SIZE;
	y_pixels = y * TILE_SIZE;
	mlx_clear_window(game->mlx, game->win);
	mlx_put_image_to_window(game->mlx, game->win, img, x_pixels, y_pixels);
}

// Dibuja el mapa
void	draw_map(t_game *game)
{
	static int	x = 0;
	static int	y = 0;

	if (y < game->height)
	{
		if (x < game->width)
		{
			clear_and_draw_tile(game, x, y);
			x++;
		}
		if (x == game->width)
		{
			x = 0;
			y++;
		}
		draw_map(game);
	}
	else
	{
		x = 0;
		y = 0;
	}
}

// Dibuja al jugador
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

// Muestra el número de movimientos
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

// Renderiza el juego
int	render_game(t_game *game)
{
	if (!game)
		return (1);
	draw_map(game);
	draw_player(game);
	show_moves(game);
	return (0);
}
