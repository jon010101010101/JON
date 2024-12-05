/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 16:25:16 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 16:39:18 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <fcntl.h>

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}

/* int	main(void)
{
	char	s = 'F';
	int		fd;

	fd = open("A", O_WRONLY);
	ft_putchar_fd(s, fd);
	return (0);
}
 */
// DESCRIPCION. Envía el carácter ’c’ al file descriptor especificado 

// DESCRIPTOR ESPECIFICADO (FD). (si es es entrada por teclado, si es 1 salida
// por pantalla, salida por impresora, etc..)

// PARAMETROS. 
// c: El carácter a enviar.
// fd: El file descriptor sobre el que escribir.

// DESCRIPTOR DE ARCHIVO. es un número entero que identifica un archivo
// abierto en un programa. 
// Cuando un programa abre un archivo, el sistema operativo le asigna un 
// descriptor de archivo único. Este descriptor de archivo se utiliza luego 
// para realizar operaciones de lectura, escritura y otras operaciones 
// relacionadas con ese archivo.

// Con fd = open("a", O_WRONLY);, abre un archivo y escribe el 
// caracter (en este caso A)
// O_WRONLY. indica que el archivo será abierto solo para escritura

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