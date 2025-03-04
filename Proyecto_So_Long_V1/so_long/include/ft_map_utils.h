/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_map_utils.h                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/02 19:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/02 18:48:42 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_MAP_UTILS_H
# define FT_MAP_UTILS_H

# include "so_long.h"

void	print_map(t_game *game);
int		check_borders(t_game *game);
int		check_elements(t_game *game, int *player_count);
int		validate_map(t_game *game);

#endif
