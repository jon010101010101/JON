#include "so_long.h"
#include "libft.h"

bool process_line(t_game *game, char *line)
{
    if (!game->map_width)
        game->map_width = ft_strlen(line);
    else if ((int)game->map_width != (int)ft_strlen(line))
        return false;

    return save_line(game, line);
}
