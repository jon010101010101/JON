#include "../include/so_long.h"
#include <stdlib.h> // Necesario para EXIT_FAILURE

void init_game(t_game *game) {
    game->mlx = mlx_init();
    game->win = NULL;
    game->map = NULL;
    game->width = 0;
    game->height = 0;
}

int main(int argc, char **argv) {
    t_game game;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <map_file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    init_game(&game);

    if (load_map(&game, argv[1]) < 0) {
        close_window(&game); // Limpiar recursos antes de salir
        return EXIT_FAILURE;
    }

    load_images(&game);

    printf("Before rendering: Width = %d, Height = %d\n", game.width, game.height);

    game.win = mlx_new_window(game.mlx, game.width * TILE_SIZE, game.height * TILE_SIZE, "So Long");
    if (!game.win) {
        fprintf(stderr, "Error: Could not create window\n");
        close_window(&game); // Limpiar recursos antes de salir
        return EXIT_FAILURE;
    }

    render_game(&game);

    mlx_key_hook(game.win, key_press, &game);
    mlx_hook(game.win, 17, 0, close_window, &game);

    mlx_loop(game.mlx);

    return 0;
}
