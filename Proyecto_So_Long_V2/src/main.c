#include <so_long.h>

int main(int argc, char **argv)
{
    t_game *game = init_game();

    if (argc != 2)
        return handle_error(game, "Usage: ./so_long map.ber");

    if (!parse_map(game, argv[1]))
        return handle_error(game, "Error parsing map");

    if (!load_images(game))
        return handle_error(game, "Error loading images");

    init_window(game); // Inicializar la ventana
    mlx_hook(game->win, 2, 1L<<0, key_press, game);
    mlx_hook(game->win, 17, 0, close_window, game);
    mlx_loop_hook(game->mlx, render_game, game);
    mlx_loop(game->mlx); // Bucle principal del juego
    return 0;
}
