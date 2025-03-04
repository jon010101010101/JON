#include "include/so_long.h"
#include "include/ft_load_map.h"
#include "include/ft_error.h"

int	main(int argc, char **argv)
{
	t_game	*game;

	game = malloc(sizeof(t_game));
	if (!game)
		return (1);
	if (argc != 2)
		handle_error("Usage: ./so_long map.ber\n", game, 0);
	if (ft_strrchr(argv[1], '.') == NULL || ft_strncmp(ft_strrchr(argv[1], '.'),
			".ber", 4) != 0)
		handle_error("Error: Invalid map extension\n", game, 0);
	load_map(game, argv[1]);
	return (0);
}
