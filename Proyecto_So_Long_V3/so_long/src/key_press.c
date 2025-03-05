/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   key_press.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:10:34 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>
#include <stdlib.h>

int		is_valid_move(t_game *game, int x, int y);
void	update_player_position(t_game *game, int keycode);
void	check_win_condition(t_game *game);
void	close_game(t_game *game);

int	key_press(int keycode, t_game *game)
{
	if (keycode == 65307)
	{
		close_game(game);
	}
	update_player_position(game, keycode);
	render_game(game);
	return (0);
}

int	is_valid_move(t_game *game, int x, int y)
{
	return (x >= 0 && x < game->width
		&& y >= 0 && y < game->height
		&& game->map[y][x] != '1');
}

void	update_player_position(t_game *game, int keycode)
{
	int	new_x;
	int	new_y;

	new_x = game->player_x;
	new_y = game->player_y;
	if (keycode == 65362 || keycode == 119)
		new_y--;
	else if (keycode == 65364 || keycode == 115)
		new_y++;
	else if (keycode == 65361 || keycode == 97)
		new_x--;
	else if (keycode == 65363 || keycode == 100)
		new_x++;
	if (is_valid_move(game, new_x, new_y))
	{
		game->map[game->player_y][game->player_x] = '0';
		game->player_x = new_x;
		game->player_y = new_y;
		game->moves++;
		printf("Moves: %d\n", game->moves);
		check_win_condition(game);
	}
	else
		printf("Movimiento inválido.\n");
}

void	check_win_condition(t_game *game)
{
	if (game->map[game->player_y][game->player_x] == 'E')
	{
		printf("¡Felicidades! ¡Has llegado a la meta!\n");
		close_game(game);
	}
}

void	close_game(t_game *game)
{
	printf("Cerrando el juego.\n");
	close_window(game);
}
