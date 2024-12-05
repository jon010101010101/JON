/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 20:14:04 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:28:47 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stddef.h>

void	*calloc(size_t count, size_t size)
{
	

//Asigna un bloque de memoria lo suficientemente grande como para contener
//count elementos de tamaño size. Devuelve el puntero al comienzo 
//de la memoria asignada. Si falla devuelve NULL