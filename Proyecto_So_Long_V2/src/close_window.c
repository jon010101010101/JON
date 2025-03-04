#include <so_long.h>

int close_window(t_game *game)
{
    if (!game)
        return 0;
    free_map(game);
    mlx_destroy_window(game->mlx, game->win);
    mlx_destroy_display(game->mlx);
    free(game->mlx);
    free(game);
    exit(0);
}
