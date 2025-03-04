#include <so_long.h>

int handle_error(t_game *game, char *message)
{
    ft_printf("Error: %s\n", message);
    if (game)
        free_map(game);
    exit(1);
}
