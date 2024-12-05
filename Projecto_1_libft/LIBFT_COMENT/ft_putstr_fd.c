/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 16:52:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 16:49:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putstr_fd(char *s, int fd)
{
	while (*s != '\0')
	{
		write(fd, s, 1);
		s++;
	}
}
/*
int	main(void)
{
	char	cadena []= "La prueba da bien!";
	int		fd;

	fd = open("A", O_WRONLY);
	ft_putstr_fd(cadena, fd);
	return (0);
}
*/
// DESCRIPCION. Envía la string ’s’ al file descriptor especificado.

// PARAMETROS. 
// c: El carácter a enviar.
// fd: El file descriptor sobre el que escribir.

// DESCRIPTOR ESPECIFICADO (FD). (si es es entrada por teclado, si es 1 salida
// por pantalla, salida por impresora, etc..)

/* // Función para escribir una cadena seguida de un salto de línea en un 
descriptor de archivo //
void ft_putstr_fd(char *s, int fd)
{
	// Iteramos sobre la cadena s hasta que lleguemos al carácter nulo '\0'
	while (*s != '\0')
	{
		// Escribimos el carácter actual de s en el descriptor de archivo 
		fd usando la función write
		write(fd, s, 1);
		// Avanzamos al siguiente carácter en s
		s++;
	}
} */