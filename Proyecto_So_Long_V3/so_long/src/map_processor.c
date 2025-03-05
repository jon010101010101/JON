/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   map_processor.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:14:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include "../libft/libft.h"
#include <stdio.h>

// Procesa una línea leída del archivo
int	process_read_line(char *buffer, t_game *game, int fd)
{
	char	*newline;
	int		line_length;

	newline = ft_strchr(buffer, '\n');
	if (newline)
		*newline = '\0';
	line_length = ft_strlen(buffer);
	if (game->width == 0)
		game->width = line_length;
	else if (line_length != game->width)
		return (handle_error("Inconsistent line length in map file", fd));
	game->map[game->height] = ft_strdup(buffer);
	if (!game->map[game->height])
		return (handle_error("Could not allocate memory for map line", fd));
	return (line_length);
}

// Procesa el archivo
int	process_line(char *buffer, t_game *game, int height)
{
	int	i;
	int	len;

	len = (int)ft_strlen(buffer);
	i = 0;
	while (i < len)
	{
		if (buffer[i] == 'E')
			game->exit_count++;
		else if (buffer[i] == 'C')
			game->collectibles++;
		else if (buffer[i] == 'P')
		{
			game->player_x = i;
			game->player_y = height;
		}
		i++;
	}
	return (0);
}

// Procesa una línea del mapa
int	process_map_line(char *line_start, t_game *game, int total_height)
{
	int	line_length;

	line_length = (int)ft_strlen(line_start);
	if (game->width == 0)
		game->width = line_length;
	else if (line_length != game->width)
		return (handle_error("Inconsistent line length in map file", -1));
	if (total_height >= MAX_MAP_HEIGHT)
		return (handle_error("Map exceeds maximum height", -1));
	game->map[total_height] = ft_strdup(line_start);
	if (!game->map[total_height])
		return (handle_error("Could not allocate memory for map line", -1));
	process_line(line_start, game, total_height);
	return (0);
}
