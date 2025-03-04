#include "../include/so_long.h"
#include "../libft/libft.h"

int validate_map(t_game *game) {
    int player_count = 0;

    // Verificar bordes
    for (int x = 0; x < game->width; x++) {
        if (game->map[0][x] != '1' || game->map[game->height - 1][x] != '1') {
            ft_printf("Error: Borde superior o inferior no válido en x=%d\n", x);
            return 0;
        }
    }
    for (int y = 0; y < game->height; y++) {
        if (game->map[y][0] != '1' || game->map[y][game->width - 1] != '1') {
            ft_printf("Error: Borde izquierdo o derecho no válido en y=%d\n", y);
            return 0;
        }
    }

    // Contar elementos y verificar caracteres válidos
    for (int y = 0; y < game->height; y++) {
        for (int x = 0; x < game->width; x++) {
            char c = game->map[y][x];
            if (c == 'P') player_count++;
            else if (c != '0' && c != '1' && c != 'C' && c != 'E') {
                ft_printf("Error: Carácter no válido '%c' en (%d, %d)\n", c, x, y);
                return 0;
            }
        }
    }

    ft_printf("Jugadores: %d, Salidas: %d, Coleccionables: %d\n",
              player_count, game->exit_count, game->collectibles);

    if (player_count != 1) {
        ft_printf("Error: Debe haber exactamente un jugador\n");
        return 0;
    }
    if (game->exit_count == 0) {
        ft_printf("Error: Debe haber al menos una salida\n");
        return 0;
    }
    if (game->collectibles == 0) {
        ft_printf("Error: Debe haber al menos un coleccionable\n");
        return 0;
    }

    return 1; // Mapa válido
}
