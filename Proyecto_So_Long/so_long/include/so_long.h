#ifndef SO_LONG_H
#define SO_LONG_H

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include "../minilibx-linux/mlx.h"
#include "../libft/libft.h"

// Definición de constantes
#define TILE_SIZE 64
#define MAX_MAP_HEIGHT 100
#define MAX_MAP_WIDTH 100

// Definición de teclas (ajusta según tu sistema)
#define KEY_ESC 65307
#define KEY_W 119
#define KEY_A 97
#define KEY_S 115
#define KEY_D 100
#define KEY_UP 65362
#define KEY_DOWN 65364
#define KEY_LEFT 65361
#define KEY_RIGHT 65363

// Definición de la estructura t_game
typedef struct s_game {
    void *mlx;
    void *win;
    char **map;
    int width;
    int height;
    int player_x;
    int player_y;
    int exit_x;
    int exit_y;
    int collectibles;
    int collected;
    int exit_count;
    int moves;
    void *img_wall;
    void *img_empty;
    void *img_collectible;
    void *img_exit;
    void *img_player;
    int img_width;
    int img_height;
} t_game;

// Declaraciones de funciones
void init_game(t_game *game);
int load_map(t_game *game, const char *filename);
void load_images(t_game *game);
int key_press(int keycode, t_game *game);
int render_game(t_game *game);
int close_window(void *param);
int is_valid_move(t_game *game, int x, int y);
void update_player_position(t_game *game, int new_x, int new_y);
void print_moves(t_game *game);
int check_win_condition(t_game *game);
void error_exit(const char *message);
void warning(const char *message);
void debug_log(const char *message);

#endif // SO_LONG_H
