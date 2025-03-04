#include <so_long.h>

bool is_map_closed(t_game *game)
{
    int i = 0;
    while (game->map[i]) {
        int j = 0;
        while (game->map[i][j]) {
            if ((i == 0 || i == game->map_height - 1 || j == 0 || j == game->map_width - 1) && game->map[i][j] != '1')
                return false;
            j++;
        }
        i++;
    }
    return true;
}
