/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 19:23:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SO_LONG_H
# define SO_LONG_H

# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <fcntl.h>
# include "../libft/libft.h"
# include <mlx.h>

# define MAX_MAP_WIDTH 400
# define MAX_MAP_HEIGHT 400
# define TILE_SIZE 32

// Define las teclas
# define KEY_ESC 53
# define KEY_W 13
# define KEY_A 0
# define KEY_S 1
# define KEY_D 2
# define KEY_UP 126
# define KEY_LEFT 123
# define KEY_DOWN 125
# define KEY_RIGHT 124

typedef struct s_game
{
	void	*mlx;
	void	*win;
	char	**map;
	int		width;
	int		height;
	int		player_x;
	int		player_y;
	int		exit_x;
	int		exit_y;
	int		collectibles;
	int		collected;
	int		exit_count;
	int		moves;
	int		win_condition;
	void	*img_wall;
	void	*img_empty;
	void	*img_collectible;
	void	*img_exit;
	void	*img_player;
	int		img_width;
	int		img_height;
}	t_game;

typedef struct s_image_map
{
	char	tile;
	void	*img;
}	t_image_map;

// Function declarations
void	init_game(t_game *game);
void	init_mlx_and_map(t_game *game);
void	init_player_and_images(t_game *game);
void	init_game_values(t_game *game);
void	create_window(t_game *game);
int		key_press(int keycode, t_game *game);
int		is_valid_move(t_game *game, int x, int y);
void	update_player_position(t_game *game, int keycode);
void	check_win_condition(t_game *game);
void	close_game(t_game *game);
int		close_window(void *param);
int		render_game(t_game *game);
void	clear_and_draw_tile(t_game *game, int x, int y);
void	draw_map(t_game *game);
void	draw_player(t_game *game);
void	show_moves(t_game *game);
void	print_moves(t_game *game);
int		handle_error(const char *message, int fd);
void	calculate_new_position(int keycode, int *new_x, int *new_y);
void	update_map(t_game *game, int new_x, int new_y);
int		load_map(t_game *game, const char *filename);
void	init_game_variables(t_game *game);
int		allocate_map_memory(t_game *game, int fd);
int		open_map_file(const char *filename);
int		load_and_validate_map(int fd, t_game *game);
int		read_map_from_file(int fd, t_game *game);
int		process_map_line(char *line_start, t_game *game, int total_height);
int		process_read_line(char *buffer, t_game *game, int fd);
int		process_line(char *buffer, t_game *game, int height);
int		validate_map(t_game *game);
int		validate_horizontal_borders(t_game *game);
int		validate_vertical_borders(t_game *game);
int		validate_map_elements(t_game *game, int *player_count);
int		validate_map_rules(t_game *game, int player_count);
int		handle_lseek(int fd, ssize_t read_bytes, char *buffer);
void	load_images(t_game *game);
void	close_game(t_game *game);
void	destroy_images_part1(t_game *game);
void	destroy_images_part2(t_game *game);
void	destroy_window_and_display(t_game *game);

#endif
