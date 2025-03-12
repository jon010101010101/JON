/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   player.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 19:14:55 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>

// Auxiliary functions
void	calculate_new_position(int keycode, int *new_x, int *new_y);
void	update_map(t_game *game, int new_x, int new_y);

// Function to update the player's position
void	update_player_position(t_game *game, int keycode)
{
	int	new_x;
	int	new_y;

	new_x = game->player_x;
	new_y = game->player_y;
	calculate_new_position(keycode, &new_x, &new_y);
	if (is_valid_move(game, new_x, new_y))
	{
		update_map(game, new_x, new_y);
		game->player_x = new_x;
		game->player_y = new_y;
		game->moves++;
		render_game(game);
		print_moves(game);
	}
	else
		printf("Movimiento inválido.\n");
}

// Auxiliary function to calculate the new position
void	calculate_new_position(int keycode, int *new_x, int *new_y)
{
	if (keycode == 65362 || keycode == 119)
		(*new_y)--;
	else if (keycode == 65364 || keycode == 115)
		(*new_y)++;
	else if (keycode == 65361 || keycode == 97)
		(*new_x)--;
	else if (keycode == 65363 || keycode == 100)
		(*new_x)++;
}

// Auxiliary function to update the map
void	update_map(t_game *game, int new_x, int new_y)
{
	char	current_tile;

	current_tile = game->map[new_y][new_x];
	if (game->map[game->player_y][game->player_x] == 'P')
		game->map[game->player_y][game->player_x] = '0';
	if (current_tile == 'C')
	{
		game->collected++;
		game->map[new_y][new_x] = '0';
	}
	else if (current_tile == 'E')
	{
		if (game->collected == game->collectibles)
		{
			printf("You win! Total moves: %d\n", game->moves + 1);
			close_game(game);
			return ;
		}
		else
			printf("You must collect all the collectibles.\n");
	}
	game->player_x = new_x;
	game->player_y = new_y;
	if (current_tile != 'E')
		game->map[new_y][new_x] = 'P';
}

// Function to check if the move is valid
int	is_valid_move(t_game *game, int x, int y)
{
	if (x < 0 || x >= game->width || y < 0 || y >= game->height)
		return (0);
	if (game->map[y][x] == '1')
		return (0);
	return (1);
}
