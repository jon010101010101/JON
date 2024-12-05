/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:57:49 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:29:48 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stddef.h>

void	*ft_memcpy(void *restrict dst, const void *restrict src, size_t n)
{


// Copia un bloque de memoria desde src a dst, el n número de bytes