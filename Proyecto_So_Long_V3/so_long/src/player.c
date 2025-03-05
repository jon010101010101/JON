/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   player.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/03/04 12:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/05 13:38:45 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"
#include <stdio.h>

// Funciones auxiliares
void calculate_new_position(int keycode, int *new_x, int *new_y);
void update_map(t_game *game, int new_x, int new_y);

// Función para actualizar la posición del jugador
void update_player_position(t_game *game, int keycode)
{
    int new_x = game->player_x;
    int new_y = game->player_y;

    // Calculate new position based on keycode
    calculate_new_position(keycode, &new_x, &new_y);

    // Check if the move is valid
    if (is_valid_move(game, new_x, new_y)) {
        // Update map
        update_map(game, new_x, new_y);

        game->player_x = new_x;
        game->player_y = new_y;
        game->moves++;

        // Update display
        render_game(game);
        print_moves(game);
    } else {
        printf("Movimiento inválido.\n");
    }
}

// Función auxiliar para calcular la nueva posición
void calculate_new_position(int keycode, int *new_x, int *new_y)
{
    if (keycode == 65362 || keycode == 119) // Up
        (*new_y)--;
    else if (keycode == 65364 || keycode == 115) // Down
        (*new_y)++;
    else if (keycode == 65361 || keycode == 97) // Left
        (*new_x)--;
    else if (keycode == 65363 || keycode == 100) // Right
        (*new_x)++;
}

// Función auxiliar para actualizar el mapa
void update_map(t_game *game, int new_x, int new_y)
{
    game->map[game->player_y][game->player_x] = '0';
    if (game->map[new_y][new_x] == 'C') {
        game->collected++;
        game->map[new_y][new_x] = '0'; // Clear collectible from map
    } else if (game->map[new_y][new_x] == 'E') {
        if (game->collected == game->collectibles) {
            printf("You win! Total moves: %d\n", game->moves + 1);
            close_game(game);
            return;
        } else {
            printf("Debes recoger todos los coleccionables.\n");
            return;
        }
    }
    game->map[new_y][new_x] = 'P';
}

// Función para verificar si el movimiento es válido
int is_valid_move(t_game *game, int x, int y)
{
    if (x < 0 || x >= game->width || y < 0 || y >= game->height)
        return 0;
    if (game->map[y][x] == '1')
        return 0;
    return 1;
}
