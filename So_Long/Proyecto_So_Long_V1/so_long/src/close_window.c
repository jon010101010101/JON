#include "../include/so_long.h"
#include <stdlib.h>

static void free_map(char **map, int height)
{
    int i;

    if (map)
    {
        for (i = 0; i < height; i++)
        {
            if (map[i])
                free(map[i]);
        }
        free(map);
    }
}

int close_window(void *param)
{
    t_game *game;

    game = (t_game *)param;
    if (game)
    {
        if (game->mlx)
        {
            if (game->img_wall)
                mlx_destroy_image(game->mlx, game->img_wall);
            if (game->img_empty)
                mlx_destroy_image(game->mlx, game->img_empty);
            if (game->img_collectible)
                mlx_destroy_image(game->mlx, game->img_collectible);
            if (game->img_exit)
                mlx_destroy_image(game->mlx, game->img_exit);
            if (game->img_player)
                mlx_destroy_image(game->mlx, game->img_player);
            if (game->win)
                mlx_destroy_window(game->mlx, game->win);
            mlx_destroy_display(game->mlx);
            free(game->mlx);
        }
        free_map(game->map, game->height);
    }
    exit(0);
    return (0);
}
