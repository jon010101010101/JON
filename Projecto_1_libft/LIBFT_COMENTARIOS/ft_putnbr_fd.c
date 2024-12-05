/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 18:23:22 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 16:48:04 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	int	divider;

	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		return ;
	}
	if (n < 0)
	{
		ft_putchar_fd('-', fd);
		n = -n;
	}
	divider = 1;
	while (n / divider >= 10)
		divider *= 10;
	while (divider != 0)
	{
		ft_putchar_fd((n / divider) + '0', fd);
		n %= divider;
		divider /= 10;
	}
}
/*
int	main(void)
{
	int	number;
	int	fd;

	number = -12345;
	fd = open("A", O_WRONLY);
	ft_putnbr_fd(number, fd);
	return (0);
}
*/
// DESCRIPCION. Envía el número ’n’ al file descriptor dado.

// PARAMETROS. 
// n: El número que enviar.
// fd: El file descriptor sobre el que escribir.

// Convierte un número entero en una cadena de caracteres y luego imprime
// esa cadena en un descriptor de archivo específico, todo mientras maneja
// correctamente los casos especiales y el signo del número.

// tiene que manejar el signo, y tener en cuenta los limites int.

// DESCRIPTOR ESPECIFICADO (FD). (si es es entrada por teclado, si es 1 salida
// por pantalla, salida por impresora, etc..)

/* // Función para escribir un número entero seguido de un salto de línea en 
un descriptor de archivo //
void ft_putnbr_fd(int n, int fd)
{
	int divisor; // Variable para almacenar el divisor

	// Verificamos si el número es el valor mínimo de un entero de 32 bits
	if (n == -2147483648)
	{
		// Si es el caso, escribimos la cadena "-2147483648" en el descriptor
		 de archivo y salimos de la función
		write(fd, "-2147483648", 11);
		return ;
	}

	// Verificamos si el número es negativo
	if (n < 0)
	{
		// Si es negativo, escribimos el signo '-' en el descriptor de archivo
		 y multiplicamos n por -1 para hacerlo positivo
		ft_putchar_fd('-', fd);
		n = -n;
	}

	divisor = 1; // Inicializamos el divisor a 1

	// Encontramos el divisor adecuado para el número
	while (n / divisor >= 10)
		divisor *= 10;

	// Mientras el divisor sea diferente de cero, continuamos dividiendo n y 
	escribiendo los dígitos en el descriptor de archivo
	while (divisor != 0)
	{
		// Escribimos el dígito más significativo de n en el descriptor de
		 archivo y lo convertimos en un carácter
		ft_putchar_fd((n / divisor) + '0', fd);
		// Actualizamos n para eliminar el dígito más significativo
		n %= divisor;
		// Actualizamos el divisor para considerar el siguiente dígito
		divisor /= 10;
	}
}
 */