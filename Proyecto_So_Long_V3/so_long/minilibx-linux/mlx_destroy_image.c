/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlx_destroy_image.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/10/03 18:56:35 by mg                #+#    #+#             */
/*   Updated: 2025/03/04 17:51:18 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "mlx_int.h"

int	mlx_destroy_image(t_xvar *xvar, t_img *img)
{
	if (img->type == MLX_TYPE_SHM_PIXMAP
		|| img->type == MLX_TYPE_SHM)
	{
		XShmDetach(xvar->display, &(img->shm));
		shmdt(img->shm.shmaddr);
	}
	XDestroyImage(img->image);
	XFreePixmap(xvar->display, img->pix);
	if (img->gc)
		XFreeGC(xvar->display, img->gc);
	free(img);
	if (xvar->do_flush)
		XFlush(xvar->display);
}
