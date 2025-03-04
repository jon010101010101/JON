#include <so_long.h>

void init_window(t_game *game)
{
    game->mlx = mlx_init();
    game->win = mlx_new_window(game->mlx, game->map_width * game->tile_size,
                              game->map_height * game->tile_size, "So Long");
}

t_game *init_game()
{
    t_game *game = malloc(sizeof(t_game));
    game->mlx = NULL;
    game->win = NULL;
    game->map = NULL;
    game->map_width = 0;
    game->map_height = 0;
    game->tile_size = 64;
    game->player_x = 0;
    game->player_y = 0;
    game->moves = 0;
    game->collected = 0;
    game->wall = NULL;
    game->floor = NULL;
    game->player = NULL;
    game->collectible = NULL;
    game->exit = NULL;
    return game;
}
