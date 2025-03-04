#include "../include/so_long.h"
#include <stdlib.h>

void destroy_image(t_game *game, void *img) {
    if (img) {
        mlx_destroy_image(game->mlx, img);
        img = NULL; // Establecer a NULL para evitar doble liberación
    }
}

void free_map(char **map, int height) {
    if (map) {
        for (int i = 0; i < height; i++) {
            if (map[i]) {
                free(map[i]);
                map[i] = NULL;
            }
        }
        free(map);
        map = NULL;
    }
}

int close_window(t_game *game) {
    if (game) {
        if (game->mlx) {
            destroy_image(game, game->img_wall);
            destroy_image(game, game->img_empty);
            destroy_image(game, game->img_collectible);
            destroy_image(game, game->img_exit);
            destroy_image(game, game->img_player);

            if (game->win) {
                mlx_destroy_window(game->mlx, game->win);
                game->win = NULL;
            }

            free(game->mlx); // Liberar la instancia de mlx
            game->mlx = NULL;
        }

        free_map(game->map, game->height);
        game->map = NULL;
    }
    exit(0);
    return 0;
}
