#include "../include/so_long.h"

typedef struct s_image_map
{
    char key;
    void *img;
} t_image_map;

void render_position(t_game *game, int x, int y, t_image_map *img_map)
{
    if (x < 0 || x >= game->width || y < 0 || y >= game->height)
        return;

    char tile = game->map[y][x];

    while (img_map->key != '\0')
    {
        if (img_map->key == tile)
        {
            mlx_put_image_to_window(game->mlx, game->win, img_map->img, x * TILE_SIZE, y * TILE_SIZE);
            break;
        }
        img_map++;
    }
}

void render_recursive(t_game *game, int x, int y, t_image_map *img_map)
{
    if (y >= game->height)
        return;
    if (x >= game->width)
    {
        render_recursive(game, 0, y + 1, img_map);
        return;
    }

    render_position(game, x, y, img_map);
    render_recursive(game, x + 1, y, img_map);
}

void print_current_map(t_game *game)
{
    printf("Current map state:\n");
    for (int y = 0; y < game->height; y++)
    {
        for (int x = 0; x < game->width; x++)
        {
            printf("%c", game->map[y][x]);
        }
        printf("\n");
    }
}

int render_game(t_game *game)
{
    mlx_clear_window(game->mlx, game->win);

    t_image_map img_map[] =
    {
        {'1', game->img_wall},
        {'0', game->img_empty},
        {'C', game->img_collectible},
        {'E', game->img_exit},
        {'P', game->img_player},
        {'\0', NULL}
    };

    printf("Before rendering: Width = %d, Height = %d\n", game->width, game->height);
    print_current_map(game);
    render_recursive(game, 0, 0, img_map);
    return 0;
}
