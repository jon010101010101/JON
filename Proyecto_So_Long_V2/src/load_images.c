#include <so_long.h>

bool load_images(t_game *game)
{
    game->wall = load_image(game, "textures/wall.xpm");
    game->floor = load_image(game, "textures/floor.xpm");
    game->player = load_image(game, "textures/player.xpm");
    game->collectible = load_image(game, "textures/collectible.xpm");
    game->exit = load_image(game, "textures/exit.xpm");
    return (game->wall && game->floor && game->player && game->collectible && game->exit);
}

void *load_image(t_game *game, char *path)
{
    void *img = mlx_xpm_file_to_image(game->mlx, path, &game->tile_size, &game->tile_size);
    return img;
}
