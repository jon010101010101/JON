#include "../include/so_long.h"
#include "../libft/libft.h"  // Asegúrate de incluir el encabezado de libft

void print_moves(t_game *game)
{
    ft_putstr_fd("Moves: ", 1);
    ft_putnbr_fd(game->moves, 1);
    ft_putchar_fd('\n', 1);
}

void clean_exit(t_game *game)
{
    if (game)
    {
        close_window(game);  // Asegúrate de que esta función maneje la liberación de recursos
    }
}
