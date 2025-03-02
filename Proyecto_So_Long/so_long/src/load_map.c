#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>

void print_map(t_game *game) {
    ft_printf("Mapa cargado:\n");
    for (int y = 0; y < game->height; y++) {
        ft_printf("%s\n", game->map[y]);
    }
}

int validate_map(t_game *game) {
    int player_count = 0;

    // Verificar bordes
    for (int x = 0; x < game->width; x++) {
        if (game->map[0][x] != '1' || game->map[game->height - 1][x] != '1') {
            ft_printf("Error: Borde superior o inferior no válido en x=%d\n", x);
            return 0;
        }
    }
    for (int y = 0; y < game->height; y++) {
        if (game->map[y][0] != '1' || game->map[y][game->width - 1] != '1') {
            ft_printf("Error: Borde izquierdo o derecho no válido en y=%d\n", y);
            return 0;
        }
    }

    // Contar elementos y verificar caracteres válidos
    for (int y = 0; y < game->height; y++) {
        for (int x = 0; x < game->width; x++) {
            char c = game->map[y][x];
            if (c == 'P') player_count++;
            else if (c != '0' && c != '1' && c != 'C' && c != 'E') {
                ft_printf("Error: Carácter no válido '%c' en (%d, %d)\n", c, x, y);
                return 0;
            }
        }
    }

    ft_printf("Jugadores: %d, Salidas: %d, Coleccionables: %d\n", 
              player_count, game->exit_count, game->collectibles);

    if (player_count != 1) {
        ft_printf("Error: Debe haber exactamente un jugador\n");
        return 0;
    }
    if (game->exit_count == 0) {
        ft_printf("Error: Debe haber al menos una salida\n");
        return 0;
    }
    if (game->collectibles == 0) {
        ft_printf("Error: Debe haber al menos un coleccionable\n");
        return 0;
    }

    return 1; // Mapa válido
}

int load_map(t_game *game, const char *filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        ft_putstr_fd("Error: Could not open map file\n", 2);
        return -1;
    }

    game->map = ft_calloc(MAX_MAP_HEIGHT, sizeof(char *));
    if (!game->map) {
        close(fd);
        ft_putstr_fd("Error: Could not allocate memory for the map\n", 2);
        return -1;
    }

    game->height = 0;
    game->width = 0;
    game->exit_count = 0;
    game->collectibles = 0;
    char buffer[MAX_MAP_WIDTH + 1];
    ssize_t read_bytes;

    while ((read_bytes = read(fd, buffer, MAX_MAP_WIDTH)) > 0) {
        buffer[read_bytes] = '\0';
        char *newline = ft_strchr(buffer, '\n');
        if (newline) *newline = '\0';

        int line_length = ft_strlen(buffer);
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

        for (int i = 0; i < line_length; i++) {
            if (buffer[i] == 'E') game->exit_count++;
            else if (buffer[i] == 'C') game->collectibles++;
            else if (buffer[i] == 'P') {
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

        if (newline) {
            lseek(fd, -(read_bytes - (newline - buffer + 1)), SEEK_CUR);
        }
    }

    close(fd);

    if (!validate_map(game)) {
        ft_putstr_fd("Error: Invalid map configuration\n", 2);
        return -1;
    }

    ft_printf("Map loaded: Width = %d, Height = %d, Exits = %d, Collectibles = %d\n", 
              game->width, game->height, game->exit_count, game->collectibles);
    print_map(game);

    return 0; // Carga exitosa
}
