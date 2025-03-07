#include <so_long.h>

int key_press(int keycode, t_game *game)
{
    if (keycode == KEY_ESC)
        close_window(game);
    else if (keycode == KEY_W)
        move_player(game, -1, 0);
    else if (keycode == KEY_A)
        move_player(game, 0, -1);
    else if (keycode == KEY_S)
        move_player(game, 1, 0);
    else if (keycode == KEY_D)
        move_player(game, 0, 1);
    return 0;
}
