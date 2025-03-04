#ifndef SO_LONG_H
#define SO_LONG_H

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include "../minilibx-linux/mlx.h"
#include "../libft/libft.h"

// Definición de constantes
#define TILE_SIZE 32
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
    void *mlx;       // Puntero a la instancia de MiniLibX
    void *win;       // Puntero a la ventana del juego
    char **map;      // Matriz que representa el mapa del juego
    int width;       // Ancho del mapa (en tiles)
    int height;      // Alto del mapa (en tiles)
    int player_x;    // Coordenada X del jugador (en tiles)
    int player_y;    // Coordenada Y del jugador (en tiles)
    int exit_x;      // Coordenada X de la salida (en tiles)
    int exit_y;      // Coordenada Y de la salida (en tiles)
    int collectibles; // Número total de objetos coleccionables en el mapa
    int collected;   // Número de objetos coleccionados por el jugador
     int exit_count;  //Cantidad de salidas
    int moves;       // Número de movimientos realizados por el jugador
    void *img_wall;    // Puntero a la imagen del muro
    void *img_empty;   // Puntero a la imagen del espacio vacío
    void *img_collectible; // Puntero a la imagen del coleccionable
    void *img_exit;    // Puntero a la imagen de la salida
    void *img_player;  // Puntero a la imagen del jugador
     int img_width;   //Ancho de la imagen
     int img_height;  //Alto de la imagen
} t_game;

// Declaraciones de funciones
void init_game(t_game *game);
int load_map(t_game *game, const char *filename);
void load_images(t_game *game);
int key_press(int keycode, t_game *game);
int render_game(t_game *game);
int close_window(t_game *game); // Modificado el tipo de parámetro
int is_valid_move(t_game *game, int x, int y);
void update_player_position(t_game *game, int new_x, int new_y);
void print_moves(t_game *game);
int check_win_condition(t_game *game);
void error_exit(const char *message);
void warning(const char *message);
void debug_log(const char *message);
int validate_map(t_game *game);

#endif // SO_LONG_H
