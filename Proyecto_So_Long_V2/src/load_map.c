#include <so_long.h>

bool parse_map(t_game *game, char *filename)
{
    int fd = open(filename, O_RDONLY);
    if (fd < 0)
        return false;

    game->map_width = 0;
    game->map_height = 0;
    char *line;

    while ((line = read_map_file_line(fd)) != NULL) {
        if (!process_line(game, line)) {
            free(line);
            close(fd);
            return false;
        }
        free(line);
        game->map_height++;
    }
    close(fd);
    return validate_map(game);
}
