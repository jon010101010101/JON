#ifndef SO_LONG_H
# define SO_LONG_H

# include "../libft/include/libft.h"
# include <stdio.h>
# include <stdlib.h>
# include <mlx.h>

# define MAX_MAP_WIDTH 100
# define MAX_MAP_HEIGHT 100
# define TILE_SIZE 64

typedef struct s_game
{
	void		*mlx;
	void		*win;
	char		**map;
	int			width;
	int			height;
	int			player_x;
	int			player_y;
	int			exit_count;
	int			collectibles;
	int			moves;
	void		*wall;
	void		*floor;
	void		*collectible;
	void		*exit;
	void		*player;
}	t_game;

#endif
