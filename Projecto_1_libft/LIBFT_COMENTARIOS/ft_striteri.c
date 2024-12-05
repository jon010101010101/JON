/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/22 12:53:44 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/21 11:14:22 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	i = 0;
	if (s == NULL || f == NULL)
		return ;
	while (s[i] != '\0')
	{
		f(i, &s[i]);
		i++;
	}
}
/* 
void example_function(unsigned int i, char *s)
{
		(void) i;
		if (*s >= 'a' && *s <= 'z')
			*s -= 32;
}

int	main(void)
{
	char	s[] = "Let's see if it works";
	ft_striteri(s, &example_function);
	printf("the string created after f is: %s\n", s);
	return (0);
} */
// DESCRIPCION. A cada carácter de la string ’s’, aplica la función
// ’f’ dando como parámetros el índice de cada carácter dentro de ’s’
// y la dirección del propio carácter, que podrá modificarse si es necesario.

// No devulve nada

// PARAMETROS. 
// s: La string que iterar.
// f: La función a aplicar sobre cada carácter.

// La función ft_striteri en C aplica una función f a cada carácter de la
// cadena s, pasando también el índice de ese carácter como primer argumento 
// a la función f.

/* // Función para aplicar una función a cada carácter de una cadena, pasando
 su índice como primer argumento 

void ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int i; // Variable para almacenar el índice actual

	i = 0; // Inicializamos el índice en 0

	// Verificamos si la cadena s o la función f son NULL
	if (s == NULL || f == NULL)
		return; // Si lo son, salimos de la función

	// Recorremos la cadena s hasta encontrar el carácter nulo '\0'
	while (s[i] != '\0')
	{
		f(i, &s[i]); // Llamamos a la función f con el índice actual y la 
		dirección del carácter actual de s como argumentos
		i++; // Incrementamos el índice para pasar al siguiente carácter de s
	}
} 
Se pasa &s[i] como segundo argumento a la función f es porque f espera un 
puntero a un carácter (char *), y s[i] es un carácter individual en la cadena s.
Sin embargo, f necesita conocer la dirección de ese carácter en la memoria, no 
solo su valor. Por lo tanto, se pasa &s[i], que es la dirección de memoria del 
carácter en la posición i de la cadena s.
*/