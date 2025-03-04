/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map_utils.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:50:14 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_map_utils.h"
#include "so_long.h"
#include "../libft/libft.h"

void	print_map(t_game *game)
{
	int	y;

	ft_printf("Mapa cargado:\n");
	y = 0;
	while (y < game->height)
	{
		ft_printf("%s\n", game->map[y]);
		y++;
	}
}

int	check_borders(t_game *game)
{
	int	x;
	int	y;

	x = 0;
	while (x < game->width)
	{
		if (game->map[0][x] != '1' || game->map[game->height - 1][x] != '1')
			return (0);
		x++;
	}
	y = 0;
	while (y < game->height)
	{
		if (game->map[y][0] != '1' || game->map[y][game->width - 1] != '1')
			return (0);
		y++;
	}
	return (1);
}

int	check_elements(t_game *game, int *player_count)
{
	int	x;
	int	y;

	y = 0;
	while (y < game->height)
	{
		x = 0;
		while (x < game->width)
		{
			char c = game->map[y][x];
			if (c == 'P')
				(*player_count)++;
			else if (c != '0' && c != '1' && c != 'C' && c != 'E')
				return (0);
			x++;
		}
		y++;
	}
	return (1);
}

int	validate_map(t_game *game)
{
	int	player_count;

	player_count = 0;
	if (!check_borders(game))
		return (0);
	if (!check_elements(game, &player_count))
		return (0);
	ft_printf("Jugadores: %d, Salidas: %d, Coleccionables: %d\n",
		player_count, game->exit_count, game->collectibles);
	if (player_count != 1 || game->exit_count == 0 || game->collectibles == 0)
		return (0);
	return (1);
}
