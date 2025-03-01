#include "../include/so_long.h"

int key_press(int keycode, t_game *game)
{
    if (keycode == KEY_ESC)
        close_window(game); // Cierra el juego si se presiona ESC

    // Lógica para mover al jugador
    if (keycode == KEY_W) // Mover hacia arriba
    {
        if (is_valid_move(game, game->player_x, game->player_y - 1))
        {
            update_player_position(game, game->player_x, game->player_y - 1);
            game->moves++;
        }
    }
    else if (keycode == KEY_S) // Mover hacia abajo
    {
        if (is_valid_move(game, game->player_x, game->player_y + 1))
        {
            update_player_position(game, game->player_x, game->player_y + 1);
            game->moves++;
        }
    }
    else if (keycode == KEY_A) // Mover hacia la izquierda
    {
        if (is_valid_move(game, game->player_x - 1, game->player_y))
        {
            update_player_position(game, game->player_x - 1, game->player_y);
            game->moves++;
        }
    }
    else if (keycode == KEY_D) // Mover hacia la derecha
    {
        if (is_valid_move(game, game->player_x + 1, game->player_y))
        {
            update_player_position(game, game->player_x + 1, game->player_y);
            game->moves++;
        }
    }

    print_moves(game); // Imprime el número de movimientos realizados

    return 0;
}
