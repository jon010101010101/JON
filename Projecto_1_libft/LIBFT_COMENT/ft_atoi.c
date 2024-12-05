/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 16:55:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	result;
	int	sign;
	int	i;

	result = 0;
	sign = 1;
	i = 0;
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\r'
		|| str[i] == '\n' || str[i] == '\v' || str[i] == '\f')
		i++;
	if ((str[i] == '-') || (str[i] == '+'))
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + str[i] - '0';
		i++;
	}
	return (result * sign);
}
/*
int main()
{
	char cadena[] = "2222222242lyion";
	printf("La cadena \"%s\" convertida a entero es: %d\n", cadena, 
	ft_atoi(cadena));
	return (0);
}
*/
// Recibe una cade de caracteres, ignora los espacios, tabuladores,
// retorno carro, salto de linea, y avance pagina, y lee la cadena uno a uno
// hasta que encuentra el primer caracter que no esta del 0 al 9. Convierte
// los digitos leidos en numero entero y lo devuelve

/*
int	ft_atoi(const char *str)
{
	int	result; // Variable para almacenar el resultado
	int	sign; // Variable para almacenar el signo del número
	int	i; 

	result = 0;
	sign = 1;
	i = 0;

	// Saltar los espacios en blanco al inicio de la cadena
	while (str[i] == ' ' || str[i] == '\t' || str[i] == '\r'
		|| str[i] == '\n' || str[i] == '\v' || str[i] == '\f')
		i++;
	if ((str[i] == '-') || (str[i] == '+'))
	{
		if (str[i] == '-') // Si el primer carácter es '-', el número es negativo
			sign = -1;     // Cambiar el signo a negativo
		i++;
	}
	// Convertir la cadena de dígitos a un número entero
	while (str[i] >= '0' && str[i] <= '9') // Mientras el carácter sea un dígito
	{
		result = result * 10 + str[i] - '0'; 
		// Multiplica el resultado actual por 10. Esto es necesario para 
		desplazar los dígitos existentes a la izquierda y abrir espacio 
		para el siguiente dígito. 
		// str[i] - '0' para convertir el dígito a entero y añadirlo al
		 resultado

		i++;
	}
	return (result * sign); // Devolver el resultado multiplicado por el
	signo
}
*/