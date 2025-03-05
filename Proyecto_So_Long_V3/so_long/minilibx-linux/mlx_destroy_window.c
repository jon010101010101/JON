/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlx_destroy_window.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/10/03 18:56:35 by mg                #+#    #+#             */
/*   Updated: 2025/03/04 17:54:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "mlx_int.h"

int	mlx_destroy_window(t_xvar *xvar, t_win_list *win)
{
	t_win_list	*w;
	t_win_list	*prev;
	t_win_list	first;

	first.next = xvar->win_list;
	prev = &first;
	w = prev->next;
	while (w)
	{
		if (w == win)
			prev->next = w->next;
		else
			prev = w;
		w = w->next;
	}
	xvar->win_list = first.next;
	XDestroyWindow(xvar->display, win->window);
	XFreeGC(xvar->display, win->gc);
	free(win);
	if (xvar->do_flush)
		XFlush(xvar->display);
}
