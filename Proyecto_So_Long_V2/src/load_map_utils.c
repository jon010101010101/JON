#include <so_long.h>

char *read_map_file_line(int fd)
{
    char *line = get_next_line(fd);
    return line;
}

bool process_line(t_game *game, char *line)
{
    if (!game->map_width)
        game->map_width = ft_strlen(line);
    else if (game->map_width != ft_strlen(line))
        return false;

    return save_line(game, line);
}
