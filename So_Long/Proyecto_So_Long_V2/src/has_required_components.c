#include <so_long.h>

bool has_required_components(t_game *game)
{
    int player = 0, exit = 0, collect = 0;
    for (int i = 0; game->map[i]; i++) {
        for (int j = 0; game->map[i][j]; j++)
        {
            if (game->map[i][j] == 'P') player++;
            if (game->map[i][j] == 'E') exit++;
            if (game->map[i][j] == 'C') collect++;
        }
    }
    return (player == 1 && exit == 1 && collect > 0);
}
