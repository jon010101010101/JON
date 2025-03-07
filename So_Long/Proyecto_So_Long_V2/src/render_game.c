#include <so_long.h>

int render_game(t_game *game)
{
    for (int i = 0; game->map[i]; i++)
    {
        for (int j = 0; game->map[i][j]; j++)
        {
            render_tile(game, i, j);
        }
    }
    return 0;
}

void render_tile(t_game *game, int i, int j)
{
    int x = j * game->tile_size;
    int y = i * game->tile_size;

    mlx_put_image_to_window(game->mlx, game->win, game->floor, x, y);

    if (game->map[i][j] == '1')
        mlx_put_image_to_window(game->mlx, game->win, game->wall, x, y);
    else if (game->map[i][j] == 'P')
        mlx_put_image_to_window(game->mlx, game->win, game->player, x, y);
    else if (game->map[i][j] == 'C')
        mlx_put_image_to_window(game->mlx, game->win, game->collectible, x, y);
    else if (game->map[i][j] == 'E')
        mlx_put_image_to_window(game->mlx, game->win, game->exit, x, y);
}
