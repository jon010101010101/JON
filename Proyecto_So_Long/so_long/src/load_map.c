#include "../include/so_long.h"
#include <fcntl.h>
#include <unistd.h>

int load_map(t_game *game, const char *filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        ft_putstr_fd("Error: Could not open map file\n", 2);
        return -1;
    }

    game->map = malloc(MAX_MAP_HEIGHT * sizeof(char *));
    if (!game->map) {
        close(fd);
        ft_putstr_fd("Error: Could not allocate memory for the map\n", 2);
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
                ft_putstr_fd("Error: Inconsistent line length in map file\n", 2);
                close(fd);
                return -1;
            }

            game->map[game->height] = ft_strdup(buffer);
            if (!game->map[game->height]) {
                ft_putstr_fd("Error: Could not allocate memory for map line\n", 2);
                close(fd);
                return -1;
            }

            // Contar salidas y otros elementos
            for (int i = 0; i < line_length; i++) {
                if (buffer[i] == 'E') {
                    game->exit_count++;
                } else if (buffer[i] == 'C') {
                    game->collectibles++;
                } else if (buffer[i] == 'P') {
                    game->player_x = i;
                    game->player_y = game->height;
                }
            }

            game->height++;
            if (game->height >= MAX_MAP_HEIGHT) {
                ft_putstr_fd("Error: Map exceeds maximum height\n", 2);
                close(fd);
                return -1;
            }

            line_length = 0;
        } else {
            line_length++;
        }
    }

    if (bytes_read == -1) {
        ft_putstr_fd("Error: Failed to read from file\n", 2);
        close(fd);
        return -1;
    }

    close(fd);

    // Verificar que el mapa tiene al menos una salida
    if (game->exit_count == 0) {
        ft_putstr_fd("Error: Map must have at least one exit\n", 2);
        return -1;
    }

    ft_printf("Map loaded: Width = %d, Height = %d, Exits = %d, Collectibles = %d\n", 
              game->width, game->height, game->exit_count, game->collectibles);

    return 0; // Carga exitosa
}
