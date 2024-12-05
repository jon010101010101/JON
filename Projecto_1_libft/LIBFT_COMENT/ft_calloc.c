/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 20:14:04 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 18:43:43 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	size_t	total_size;
	void	*ptr;

	total_size = count * size;
	ptr = malloc(total_size);
	if (ptr == NULL)
		return (NULL);
	ft_bzero(ptr, total_size);
	return (ptr);
}

/* 
int main(void)
{
	int *array;
	int length = 15;
	int i;

	array = (int *)calloc(length, sizeof(int));

	if (array == NULL)
	{
		printf("Memory allocation has failed.\n");
		return (1);
	}
	i = 0;
	 while (i < length)
	{
		printf("%d ", array[i]);
		i++;
	}
	printf("\n");

	free(array);

	return (0);
}
 */
//Asigna un bloque de memoria lo suficientemente grande como para contener
//count elementos de tamaño size. Devuelve el puntero al comienzo 
//de la memoria asignada. Si falla devuelve NULL

/*
void	*ft_calloc(size_t count, size_t size)
{
	size_t	total_size; // / Variable para almacenar el tamaño total de la
						// memoria a asignar
	void	*ptr;		// // Puntero para almacenar la dirección de memoria
						// asignada

// Calcular el tamaño total de la memoria a asignar
	total_size = count * size;
// Asignar memoria utilizando malloc	
	ptr = malloc(total_size);
// Verificar si malloc se ha podido hacer	
	if (ptr == NULL)
		return (NULL);   // Devolver NULL si malloc falla
// Llenar la memoria asignada con ceros utilizando ft_bzero
	ft_bzero(ptr, total_size);
// Devolver el puntero a la memoria asignada
	return (ptr);
}
*/