/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:00:36 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:29:26 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>
#include <stddef.h>

void	*ft_memchr(const void *s, int c, size_t n)
{
	
//Se utiliza para buscar la primera aparicion de un caracter en los
// primeros n bytes de un bloque de memoria