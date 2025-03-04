#ifndef SO_LONG_H
# define SO_LONG_H

# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <fcntl.h>
# include <stdbool.h>
# include <string.h>
# include <math.h>
# include <libft.h>
# include <mlx.h>

// Define key codes
# define KEY_ESC 53
# define KEY_W 13
# define KEY_A 0
# define KEY_S 1
# define KEY_D 2

typedef struct s_game {
    void    *mlx;
    void    *win;
    char    **map;
    int     map_width;
    int     map_height;
    int     tile_size;
    int     player_x;
    int     player_y;
    int     moves;
    int     collected;
    void    *wall;
    void    *floor;
    void    *player;
    void    *collectible;
    void    *exit;
}           t_game;

// Function prototypes
t_game  *init_game();
int     main(int argc, char **argv);
bool    parse_map(t_game *game, char *filename);
bool    load_images(t_game *game);
int     render_game(t_game *game);
int     key_press(int keycode, t_game *game);
int     close_window(t_game *game);
int     handle_error(t_game *game, char *message);
void    free_map(t_game *game);
void    init_window(t_game *game);
void    move_player(t_game *game, int move_y, int move_x);
bool    check_win_condition(t_game *game);
void    render_tile(t_game *game, int i, int j);
char    *read_map_file_line(int fd);
bool    process_line(t_game *game, char *line);
bool    validate_line_length(t_game *game);
bool    is_map_rectangular(t_game *game);
bool    is_map_closed(t_game *game);
bool    has_required_components(t_game *game);
void    *load_image(t_game *game, char *path);
bool    validate_map(t_game *game);
bool    save_line(t_game *game, char *line);
void    collect_collectible(t_game *game, int new_y, int new_x);
void    update_player_position(t_game *game, int new_y, int new_x);

#endif
