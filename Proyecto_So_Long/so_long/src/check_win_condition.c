#include "../include/so_long.h"

int check_win_condition(t_game *game)
{
    // Verifica si el número de coleccionables recogidos es igual al número total de coleccionables
    // y si hay al menos una salida en el mapa
    if (game->collected == game->collectibles && game->exit_count > 0)
    {
        ft_printf("¡Felicidades! Has ganado el juego en %d movimientos.\n", game->moves);
        return 1; // Condición de victoria cumplida
    }
    return 0; // Condición de victoria no cumplida
}
