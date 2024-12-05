/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 18:17:01 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:29:38 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stddef.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	
//Se utiliza para comparar los n primeros bytes de dos bloques de memoria