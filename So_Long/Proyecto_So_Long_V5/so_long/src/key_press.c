/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   key_press.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 17:02:14 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>
#include <stdlib.h>

// Declaración de la función close_game (ahora definida en key_press.c)
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

void	close_game(t_game *game)
{
	printf("Cerrando el juego.\n");
	close_window(game);
}
