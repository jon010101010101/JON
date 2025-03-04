#include "so_long.h"
#include "libft.h"

bool validate_line_length(t_game *game)
{
    int i = 0;

    while (game->map[i] != NULL)
    {
        if ((int)ft_strlen(game->map[i]) != game->map_width)
            return (false);
        i++;
    }
    return (true);
}
