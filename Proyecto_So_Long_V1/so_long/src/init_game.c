#include "../include/so_long.h"

void init_game(t_game *game)
{
    game->mlx = mlx_init();
    if (!game->mlx)
    {
        ft_putstr_fd("Error: No se pudo inicializar MLX\n", 2);
        exit(1);
    }
    game->win = NULL;
    game->map = NULL;
    game->width = 0;
    game->height = 0;
    game->player_x = 0;
    game->player_y = 0;
    game->exit_x = 0;
    game->exit_y = 0;
    game->collectibles = 0;
    game->collected = 0;
    game->exit_count = 0;
    game->moves = 0;
    game->img_wall = NULL;
    game->img_empty = NULL;
    game->img_collectible = NULL;
    game->img_exit = NULL;
    game->img_player = NULL;
}

void load_images(t_game *game)
{
    int img_width, img_height;

    game->img_wall = mlx_xpm_file_to_image(game->mlx, "textures/wall.xpm", &img_width, &img_height);
    game->img_empty = mlx_xpm_file_to_image(game->mlx, "textures/empty.xpm", &img_width, &img_height);
    game->img_collectible = mlx_xpm_file_to_image(game->mlx, "textures/collectible.xpm", &img_width, &img_height);
    game->img_exit = mlx_xpm_file_to_image(game->mlx, "textures/exit.xpm", &img_width, &img_height);
    game->img_player = mlx_xpm_file_to_image(game->mlx, "textures/player.xpm", &img_width, &img_height);

    if (!game->img_wall || !game->img_empty || !game->img_collectible || !game->img_exit || !game->img_player)
    {
        ft_putstr_fd("Error: No se pudieron cargar una o más imágenes\n", 2);
        close_window(game);
        exit(1);
    }
}

int main(int argc, char **argv)
{
    t_game game;

    if (argc != 2)
    {
        ft_putstr_fd("Error: Uso incorrecto. Utiliza: ./so_long mapa.ber\n", 2);
        return 1;
    }

    init_game(&game);

    if (load_map(&game, argv[1]) < 0)
    {
        close_window(&game);
        return 1;
    }

    // Modificación aquí: establecemos un tamaño fijo para la ventana
    int window_width = 1280;
    int window_height = 720;
    game.win = mlx_new_window(game.mlx, window_width, window_height, "So Long");
    if (!game.win)
    {
        ft_putstr_fd("Error: No se pudo crear la ventana\n", 2);
        close_window(&game);
        return 1;
    }

    load_images(&game);
    render_game(&game);

    mlx_key_hook(game.win, key_press, &game);
    mlx_hook(game.win, 17, 0, close_window, &game);

    mlx_loop(game.mlx);

    return 0;
}
