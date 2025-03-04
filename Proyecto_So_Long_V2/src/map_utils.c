#include <so_long.h>

void free_map(t_game *game)
{
    if (!game || !game->map)
        return;
    int i = 0;
    while (game->map[i]) {
        free(game->map[i]);
        i++;
    }
    free(game->map);
    game->map = NULL;
}
