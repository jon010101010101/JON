/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   map_validation.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/04 12:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 12:26:12 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"

// Declaraciones de funciones (pueden estar en so_long.h)
int	validate_horizontal_borders(t_game *game);
int	validate_vertical_borders(t_game *game);
int	validate_map_elements(t_game *game, int *player_count);
int	validate_map_rules(t_game *game, int player_count);

int	validate_map(t_game *game)
{
	int	player_count;

	if (!validate_horizontal_borders(game))
		return (0);
	if (!validate_vertical_borders(game))
		return (0);
	if (!validate_map_elements(game, &player_count))
		return (0);
	if (!validate_map_rules(game, player_count))
		return (0);
	return (1);
}

int	validate_horizontal_borders(t_game *game)
{
	int	i;

	i = 0;
	while (i < game->width)
	{
		if (game->map[0][i] != '1' || game->map[game->height - 1][i] != '1')
			return (0);
		i++;
	}
	return (1);
}

int	validate_vertical_borders(t_game *game)
{
	int	i;

	i = 0;
	while (i < game->height)
	{
		if (game->map[i][0] != '1' || game->map[i][game->width - 1] != '1')
			return (0);
		i++;
	}
	return (1);
}

int	validate_map_elements(t_game *game, int *player_count)
{
	int	i;
	int	j;

	*player_count = 0;
	i = 0;
	while (i < game->height)
	{
		j = 0;
		while (j < game->width)
		{
			if (game->map[i][j] != '0' && game->map[i][j] != '1' &&
				game->map[i][j] != 'C' && game->map[i][j] != 'E'
				&& game->map[i][j] != 'P')
			{
				return (0);
			}
			if (game->map[i][j] == 'P')
				(*player_count)++;
			j++;
		}
		i++;
	}
	return (1);
}

int	validate_map_rules(t_game *game, int player_count)
{
	int	i;
	int	j;
	int	collectible_count;
	int	exit_count;

	collectible_count = 0;
	exit_count = 0;
	i = 0;
	while (i < game->height)
	{
		j = 0;
		while (j < game->width)
		{
			if (game->map[i][j] == 'C')
				collectible_count++;
			if (game->map[i][j] == 'E')
				exit_count++;
			j++;
		}
		i++;
	}
	if (player_count != 1 || collectible_count < 1 || exit_count != 1)
		return (0);
	return (1);
}
