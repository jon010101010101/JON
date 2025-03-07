#include "../include/so_long.h"

// Función para inicializar el juego
void init_game(t_game *game)
{
    // Inicializa MiniLibX
    game->mlx = mlx_init();
    game->win = NULL; // Inicializa la ventana como NULL
    game->map = NULL; // Inicializa el mapa como NULL
    game->width = 0; // Inicializa el ancho
    game->height = 0; // Inicializa la altura
    // Inicializa otras variables según sea necesario
}

int main(int argc, char **argv)
{
    t_game game;

    // Verifica que se haya pasado un argumento para el archivo del mapa
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <map_file>\n", argv[0]);
        return 1; // Manejo de errores si no se pasa un archivo
    }

    // Inicializa el juego
    init_game(&game);

    // Carga el mapa
    if (load_map(&game, argv[1]) < 0)
    {
        return -1; // Manejo de errores al cargar el mapa
    }

    // Carga las imágenes
    load_images(&game);

    // Imprime dimensiones antes de renderizar
    printf("Before rendering: Width = %d, Height = %d\n", game.width, game.height);

    // Crea la ventana
    game.win = mlx_new_window(game.mlx, game.width * TILE_SIZE, game.height * TILE_SIZE, "So Long");
    if (!game.win)
    {
        fprintf(stderr, "Error: Could not create window\n");
        return -1;
    }

    // Renderiza el juego
    render_game(&game);

    // Añade estos hooks:
    mlx_key_hook(game.win, key_press, &game);
    mlx_hook(game.win, 17, 0, close_window, &game);  // Para manejar el cierre de la ventana

    // Bucle principal del juego (eventos, actualización)
    mlx_loop(game.mlx);

    return 0;
}
