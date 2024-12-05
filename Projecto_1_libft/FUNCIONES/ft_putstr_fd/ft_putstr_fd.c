/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 16:52:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:33:03 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr_fd(char *s, int fd)
{
	
}

int	main(void)
{
	
}

// DESCRIPCION. Envía la string ’s’ al file descriptor especificado.

// PARAMETROS. 
// c: El carácter a enviar.
// fd: El file descriptor sobre el que escribir.

// DESCRIPTOR ESPECIFICADO (FD). (si es es entrada por teclado, si es 1 salida
// por pantalla, salida por impresora, etc..)

/* // Función para escribir una cadena en un descriptor de archivo //
void ft_putstr_fd(char *s, int fd)
{
	// Recorremos la cadena hasta que alcancemos el carácter nulo '\0'
	while (*s != '\0')
	{
		// Escribimos el carácter actual de la cadena en el descriptor de 
		archivo fd
		write(fd, s, 1);
		// Avanzamos al siguiente carácter de la cadena
		s++;
	}
} */