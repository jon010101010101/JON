#include <so_long.h>

bool check_win_condition(t_game *game)
{
    int total_collectibles = 0;
    for (int i = 0; game->map[i]; i++)
    {
        for (int j = 0; game->map[i][j]; j++)
        {
            if (game->map[i][j] == 'C')
                total_collectibles++;
        }
    }
    return (game->collected == total_collectibles);
}
