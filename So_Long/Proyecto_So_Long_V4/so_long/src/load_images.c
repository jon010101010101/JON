/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   load_images.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/07 18:52:36 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/so_long.h"

// Auxiliary function to load an image from an XPM file
static void	*load_xpm_image(
	void *mlx_ptr,
	char *filename,
	int *width,
	int *height
)

{
	void	*img_ptr;

	img_ptr = mlx_xpm_file_to_image(mlx_ptr, filename, width, height);
	return (img_ptr);
}

// Auxiliary function to check if an image was loaded correctly
void	check_image(void *img_ptr, char *filename, t_game *game)
{
	if (!img_ptr)
	{
		ft_putstr_fd("Error: Failed to load image ", 2);
		ft_putstr_fd(filename, 2);
		ft_putstr_fd("\n", 2);
		close_game(game);
		exit(EXIT_FAILURE);
	}
}

// Auxiliary function to load image dimensions
static void	store_image_dimensions(t_game *game, int width, int height)
{
	game->img_width = width;
	game->img_height = height;
	ft_printf("Images loaded successfully. ");
	ft_printf("Width: %d, Height: %d\n", width, height);
}

void	load_images(t_game *game)
{
	int	width;
	int	height;

	game->img_wall = load_xpm_image(game->mlx, "src/textures/ladrillo.xpm", \
									&width, &height);
	check_image(game->img_wall, "src/textures/ladrillo.xpm", game);
	game->img_empty = load_xpm_image(game->mlx, "src/textures/floor_black.xpm", \
									&width, &height);
	check_image(game->img_empty, "src/textures/floor_black.xpm", game);
	game->img_collectible = load_xpm_image(game->mlx, \
										"src/textures/ghost_down1.xpm", \
										&width, &height);
	check_image(game->img_collectible, "src/textures/ghost_down1.xpm", game);
	game->img_exit = load_xpm_image(game->mlx, "src/textures/door.xpm", \
									&width, &height);
	check_image(game->img_exit, "src/textures/door.xpm", game);
	game->img_player = load_xpm_image(game->mlx, "src/textures/pac_man.xpm", \
									&width, &height);
	check_image(game->img_player, "src/textures/pac_man.xpm", game);
	store_image_dimensions(game, width, height);
}
