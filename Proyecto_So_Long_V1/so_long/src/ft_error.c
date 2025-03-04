/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_error.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:49:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include "ft_error.h"

void	free_map(t_game *game)
{
	int	i;

	i = 0;
	while (i < game->height)
	{
		if (game->map[i])
			free(game->map[i]);
		i++;
	}
	free(game->map);
}

void	handle_error(char *message, t_game *game, int fd)
{
	ft_putstr_fd("Error\n", 2);
	ft_putstr_fd(message, 2);
	if (fd > 0)
		close(fd);
	if (game && game->map)
		free_map(game);
	if (game)
		free(game);
	exit(EXIT_FAILURE);
}
