/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:19:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 10:24:07 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <string.h>

int	ft_atoi(const char *str)
{
	int	result;
	int	sign;	
	int	i;
	
	result = 0;
	sign = 1;
	i = 0;
	while((str[i] == ' ' || str[i] == '\t' || str[i] == '\r'
		|| str[i] == '\n' || str[i] == '\v' || str[i] == '\f'))
		i++;
	if ((str[i] == '-') || (str[i] == '+'))
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}		
	while (str[i] > 0 && str[i] <= 9)
		result = result * 10 + str[i] - '0';
	i++;
	return (result * sign);
}

int main()
{
	char cadena[] = "       2242pepe";

	printf("La cadena \"%s\" convertida a entero es: %d\n", cadena, 
	ft_atoi(cadena));

	return (0);
}

// Recibe una cade de caracteres, ignora los espacios, signos puntuación, tabuladores, etc
//y lee la cadena uno a uno hasta que encuentra el primer caracter que no esta del 0 al 9. 
//Se detendrá en el primerr caracter no numerico y devolver los numeros leidos hasta entonces.
