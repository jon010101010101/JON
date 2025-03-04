#include "../include/so_long.h"

// Función para actualizar la posición del jugador
void update_player_position(t_game *game, int new_x, int new_y)
{
    game->map[game->player_y][game->player_x] = '0';
    
    if (game->map[new_y][new_x] == 'C') {
        game->collected++;
    } else if (game->map[new_y][new_x] == 'E' && game->collected == game->collectibles) {
        // El jugador ha ganado
        printf("You win! Total moves: %d\n", game->moves + 1);
        close_window(game);
    }
    
    game->map[new_y][new_x] = 'P';
    game->player_x = new_x;
    game->player_y = new_y;
    game->moves++;

    render_game(game);
    print_moves(game);
}


// Función para verificar si el movimiento es válido
int is_valid_move(t_game *game, int x, int y)
{
    // Verifica los límites del mapa y si la nueva posición es válida (no es una pared)
    if (x < 0 || x >= game->width || y < 0 || y >= game->height)
        return 0; // Fuera de límites

    if (game->map[y][x] == '1') // Si es una pared
        return 0;

    return 1; // Movimiento válido
}
