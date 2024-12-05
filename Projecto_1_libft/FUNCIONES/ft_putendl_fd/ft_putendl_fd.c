/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putendl_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/09 11:14:53 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:32:40 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putendl_fd(char *s, int fd)
{
	
}

int	main(void)
{
	
}

// DESCRIPCION. Envía la string ’s’ al file descriptor dado, seguido 
// de un salto de línea.

// PARAMETROS. 
// s: La string a enviar.
// fd: El file descriptor sobre el que escribir.

// DESCRIPTOR ESPECIFICADO (FD). (si es es entrada por teclado, si es 1 salida
// por pantalla, salida por impresora, etc..)

/* // Función para escribir una cadena seguida de un salto de línea en un 
descriptor de archivo //
void ft_putendl_fd(char *s, int fd)
{
	// Verificamos si la cadena es nula
	if (!s)
		return; // Si es nula, salimos de la función
	
	// Recorremos la cadena hasta alcanzar el carácter nulo '\0'
	while (*s)
		// Escribimos el carácter actual de la cadena en el descriptor
		 de archivo fd y avanzamos al siguiente carácter
		write(fd, s++, 1);
	
	// Después de escribir toda la cadena, escribimos un salto de línea 
	'\n' en el descriptor de archivo fd
	write(fd, "\n", 1);
} */