#ifndef FT_ERROR_H
# define FT_ERROR_H

# include "so_long.h"

void    free_map(t_game *game);
void    handle_error(char *message, t_game *game, int fd);

#endif
