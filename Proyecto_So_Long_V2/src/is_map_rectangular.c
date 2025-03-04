#include <so_long.h>

bool is_map_rectangular(t_game *game)
{
    int i = 0;
    while (game->map[i]) {
        if (ft_strlen(game->map[i]) != (size_t)game->map_width)
            return false;
        i++;
    }
    return true;
}
