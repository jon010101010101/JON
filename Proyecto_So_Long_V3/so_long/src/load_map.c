#include "../include/so_long.h"
#include "../libft/libft.h"
#include <fcntl.h>
#include <unistd.h>
#include <string.h> // Para strncmp
#include <stdlib.h> //Para exit

// Función auxiliar para liberar la memoria del mapa
void free_map(char **map, int height)
{
    if (map) {
        for (int i = 0; i < height; i++) {
            if (map[i]) {
                free(map[i]);
                map[i] = NULL;
            }
        }
        free(map);
        map = NULL;
    }
}

int check_ber(const char *filename)
{
    int len;

    len = ft_strlen(filename);
    if (len < 5 || ft_strncmp(filename + len - 4, ".ber", 4) != 0)
        return (0);
    return (1);
}

int load_map(t_game *game, const char *filename)
{
    int fd = open(filename, O_RDONLY);
    //char *line; // Eliminada variable no utilizada
    if (!check_ber(filename)) {
        fprintf(stderr, "Error: Map must end in .ber\n");
		exit (1);
        return (-1);
    }
    if (fd == -1) {
        fprintf(stderr, "Error: Could not open map file\n");
        return -1;
    }

    game->map = ft_calloc(MAX_MAP_HEIGHT, sizeof(char *));
    if (!game->map) {
        close(fd);
        fprintf(stderr, "Error: Could not allocate memory for the map\n");
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
        if (game->width == 0)
        {
            game->width = line_length;
        } 
        else if (line_length != game->width)
        {
            fprintf(stderr, "Error: Inconsistent line length in map file\n");
            close(fd);
            free_map(game->map, game->height);
            return -1;
        }

        game->map[game->height] = ft_strdup(buffer);
        if (!game->map[game->height])
        {
            fprintf(stderr, "Error: Could not allocate memory for map line\n");
            close(fd);
            free_map(game->map, game->height);
            return -1;
        }

        for (int i = 0; i < line_length; i++)
        {
            if (buffer[i] == 'E') game->exit_count++;
            else if (buffer[i] == 'C') game->collectibles++;
            else if (buffer[i] == 'P') {
                game->player_x = i;
                game->player_y = game->height;
            }
        }

        game->height++;
        if (game->height >= MAX_MAP_HEIGHT) {
            fprintf(stderr, "Error: Map exceeds maximum height\n");
            close(fd);
            free_map(game->map, game->height);
            return -1;
        }

        if (newline) {
            lseek(fd, -(read_bytes - (newline - buffer + 1)), SEEK_CUR);
        }
    }

    close(fd);

    if (!validate_map(game)) {
        fprintf(stderr, "Error: Invalid map configuration\n");
        free_map(game->map, game->height);
        return -1;
    }

    printf("Map loaded: Width = %d, Height = %d, Exits = %d, Collectibles = %d\n",
           game->width, game->height, game->exit_count, game->collectibles);
    //print_map(game);

    return 0; // Carga exitosa
}
