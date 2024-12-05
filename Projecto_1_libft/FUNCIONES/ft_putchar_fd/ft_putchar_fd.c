/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 16:25:16 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:32:29 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>


void	ft_putchar_fd(char c, int fd)
{
	
}

int	main(void)
{
	
}

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