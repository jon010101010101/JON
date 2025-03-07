/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_load_map.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:44:29 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_LOAD_MAP_H
# define FT_LOAD_MAP_H

# include "so_long.h"

int	process_line(t_game *game, char *buffer, int line_length);
int	read_map_file(t_game *game, int fd);
int	load_map(t_game *game, const char *filename);
int validate_and_print(t_game *game);

#endif
