/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   so_long.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:39:01 by jurrutia         ###   ########.fr       */
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

// Funciones en init_game.c
void	init_game(t_game *game);

// Funciones en load_images.c
void	load_images(t_game *game);

// Funciones en load_map.c
int		load_map(t_game *game, const char *filename);
void 	init_game_variables(t_game *game);
int     allocate_map_memory(t_game *game, int fd);
int 	open_map_file(const char *filename);
int     load_and_validate_map(int fd, t_game *game);

// Funciones en map_reader.c
int 	read_map_from_file(int fd, t_game *game);
int 	process_map_line(char *line_start, t_game *game, int total_height);

// Funciones en map_processor.c
int     process_read_line(char *buffer, t_game *game, int fd);
int 	process_line(char *buffer, t_game *game, int height);

// Funciones en map_validation.c
int		validate_map(t_game *game);
int		validate_horizontal_borders(t_game *game);
int		validate_vertical_borders(t_game *game);
int		validate_map_elements(t_game *game, int *player_count);
int		validate_map_rules(t_game *game, int player_count);

// Funciones en map_utils.c
int 	handle_lseek(int fd, ssize_t read_bytes, char *buffer);

// Funciones en key_press.c
int		key_press(int keycode, t_game *game);
int     is_valid_move(t_game *game, int x, int y);
void 	update_player_position(t_game *game, int keycode);
void 	check_win_condition(t_game *game);
void    close_game(t_game *game);

// Funciones en close_window.c
int		close_window(void *param);

// Funciones en render_game.c
int		render_game(t_game *game);
void 	clear_and_draw_tile(t_game *game, int x, int y);
void 	draw_map(t_game *game);
void 	draw_player(t_game *game);
void 	show_moves(t_game *game);

// Funciones en utils.c
void	print_moves(t_game *game);

// Funciones en error_handling.c
int		handle_error(const char *message, int fd);

// Funciones en player.c
void calculate_new_position(int keycode, int *new_x, int *new_y);
void update_map(t_game *game, int new_x, int new_y);

#endif


