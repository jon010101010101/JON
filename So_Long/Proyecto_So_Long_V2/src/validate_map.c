#include <so_long.h>

bool validate_map(t_game *game)
{
    if (!validate_line_length(game))
        return false;
    if (!is_map_rectangular(game))
        return false;
    if (!is_map_closed(game))
        return false;
    if (!has_required_components(game))
        return false;
    return true;
}
