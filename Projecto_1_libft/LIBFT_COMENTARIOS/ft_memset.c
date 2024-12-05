/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 16:06:56 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:51:06 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *b, int c, size_t len)
{
	unsigned char	*ptr;
	unsigned char	value;
	unsigned char	*end;

	ptr = b;
	value = (unsigned char)c;
	end = ptr + len;
	while (ptr < end)
	{
		*ptr = value;
		ptr++;
	}
	return (b);
}
/*
int main()
{
	char str[20];

	ft_memset(str, 'A', 20);

	printf("Después de ft_memset: %.*s\n", (int)sizeof(str), str);

	return (0);
}
*/
//Asigna el valor c a cada byte de los primeros len bytes
// del bloque de memoria apuntado por b

/*
void	*ft_memset(void *b, int c, size_t len)
{
	unsigned char	*ptr;	// Puntero a unsigned char para recorrer el bloque
							// de memoria
	unsigned char	value;	// Valor a asignar a cada byte del bloque
	unsigned char	*end;	// Puntero al final del bloque de memoria

	*ptr = b;		// Inicializamos ptr con la dirección de memoria del 
					// inicio del bloque
	b es un puntero genérico (void*), por lo que se convierte a unsigned char*
	para permitir operaciones de manipulación de datos byte a byte. Un unsigned
	char garantiza que el rango de valores sea de 0 a 255, lo cual es importante
	para asegurar que los valores se manejen correctamente sin interpretaciones 
	negativas.
	
	value = (unsigned char)c; // Convertimos c a unsigned char y lo asignamos 
							  // a value
	
	c es un entero (int), y se convierte a unsigned char para garantizar que 
	solo 	los 8 bits menos significativos se usen para llenar la memoria. 
	Esto asegura que el valor se interprete correctamente como un byte y no
	 como un entero más grande.
							  
	*end = ptr + len;
	
// Iteramos sobre cada byte del bloque de memoria
	while (ptr < end)
	{
		*ptr = value;    // Asignamos el valor a cada byte del bloque
		ptr++;
	}
	return (b);  // Devolvemos el puntero al inicio del bloque de memoria
}
*/