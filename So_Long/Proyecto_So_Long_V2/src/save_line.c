#include <so_long.h>

bool save_line(t_game *game, char *line)
{
    if (!game->map) {
        game->map = malloc(sizeof(char *) * 2);
        game->map[0] = ft_strdup(line);
        game->map[1] = NULL;
    }
    else {
        int i = 0;
        while (game->map[i])
            i++;
        game->map = realloc(game->map, sizeof(char *) * (i + 2));
        game->map[i] = ft_strdup(line);
        game->map[i + 1] = NULL;
    }
    return true;
}
