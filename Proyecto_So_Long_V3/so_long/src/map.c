#include "../include/so_long.h"
#include <fcntl.h>
#include <unistd.h>

int load_map(t_game *game, const char *filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        write(2, "Error: Could not open map file\n", 31);
        return -1;
    }

    game->map = malloc(MAX_MAP_HEIGHT * sizeof(char *));
    if (!game->map) {
        close(fd);
        write(2, "Error: Could not allocate memory for the map\n", 46);
        return -1;
    }

    game->height = 0;
    game->width = 0;
    char buffer[MAX_MAP_WIDTH + 1];
    int bytes_read;
    int line_length = 0;

    while ((bytes_read = read(fd, buffer + line_length, 1)) > 0) {
        if (buffer[line_length] == '\n' || line_length == MAX_MAP_WIDTH) {
            buffer[line_length] = '\0';
            
            if (game->width == 0) {
                game->width = line_length;
            } else if (line_length != game->width) {
                write(2, "Error: Inconsistent line length in map file\n", 45);
                close(fd);
                return -1;
            }

            game->map[game->height] = strdup(buffer);
            if (!game->map[game->height]) {
                write(2, "Error: Could not allocate memory for map line\n", 47);
                close(fd);
                return -1;
            }

            game->height++;
            if (game->height >= MAX_MAP_HEIGHT) {
                write(2, "Error: Map exceeds maximum height\n", 34);
                close(fd);
                return -1;
            }

            line_length = 0;
        } else {
            line_length++;
        }
    }

    if (bytes_read == -1) {
        write(2, "Error: Failed to read from file\n", 32);
        close(fd);
        return -1;
    }

    close(fd);
    return 0;
}
