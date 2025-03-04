#include "../include/so_long.h"

void load_images(t_game *game)
{
    int width, height;

    // Carga las imágenes desde archivos XPM con la ruta correcta
    game->img_wall = mlx_xpm_file_to_image(game->mlx, "src/textures/wall.xpm", &width, &height);
    game->img_empty = mlx_xpm_file_to_image(game->mlx, "src/textures/empty.xpm", &width, &height);
    game->img_collectible = mlx_xpm_file_to_image(game->mlx, "src/textures/collectible.xpm", &width, &height);
    game->img_exit = mlx_xpm_file_to_image(game->mlx, "src/textures/exit.xpm", &width, &height);
    game->img_player = mlx_xpm_file_to_image(game->mlx, "src/textures/player.xpm", &width, &height);

    // Verifica si las imágenes se han cargado correctamente
    if (!game->img_wall || !game->img_empty || !game->img_collectible || 
        !game->img_exit || !game->img_player)
    {
        ft_printf("Error: Failed to load one or more images\n");
        // Liberar las imágenes que se hayan cargado correctamente
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
        exit(EXIT_FAILURE); // Termina el programa si hay un error
    }

    // Almacena las dimensiones de las imágenes
    game->img_width = width;
    game->img_height = height;

    ft_printf("Images loaded successfully. Width: %d, Height: %d\n", width, height);
}
