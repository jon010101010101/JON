#include "so_long.h"
#include "libft.h"

void collect_collectible(t_game *game, int new_y, int new_x)
{
    if (game->map[new_y][new_x] == 'C')
    {
        game->collected++;
        game->map[new_y][new_x] = '0';
    }
}

void update_player_position(t_game *game, int new_y, int new_x)
{
    game->map[game->player_y][game->player_x] = '0';
    game->player_x = new_x;
    game->player_y = new_y;
    game->map[new_y][new_x] = 'P';
}

void move_player(t_game *game, int move_y, int move_x)
{
    int new_y = game->player_y + move_y;
    int new_x = game->player_x + move_x;

    if (game->map[new_y][new_x] != '1')
    {
        if (game->map[new_y][new_x] == 'E')
        {
            if (check_win_condition(game))
                close_window(game);
            return;
        }
        collect_collectible(game, new_y, new_x);
        update_player_position(game, new_y, new_x);
        game->moves++;
        ft_printf("Moves: %d\n", game->moves);
    }
}
