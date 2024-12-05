/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 17:00:36 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:41:11 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t		i;
	const char	*ptr;

	i = 0;
	ptr = (const char *)s;
	while (i < n)
	{
		if (*ptr == (char)c)
		{
			return ((void *)ptr);
		}
		ptr++;
		i++;
	}
	return (NULL);
}

/*
int main()
{
	char str[] = "Hola, Manola!";
	char *ptr;

	ptr = ft_memchr(str, 'M', 10);

	if (ptr != NULL)
	{
		printf("Caracter encontrado en la posición %ld.\n", ptr - str);
	}
	else
	{
		printf("Caracter no encontrado en los primeros bytes.\n");
	}
	return (0);
}
*/
//Se utiliza para buscar la primera aparicion de un caracter en los
// primeros n bytes de un bloque de memoria

/*
void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t		i;
	const char	*ptr;		// Puntero constante para recorrer la memoria

	i = 0;
	ptr = (const char *)s; // Convertir el puntero a char constante para
							// comparar bytes

	Esto se hace porque s es un puntero a void, lo que significa que no
	 tiene un tipo específico asociado. Para poder comparar cada byte con
	  el carácter c, necesitamos tratar los datos apuntados por s como un 
	  array de caracteres (char). De esta manera, ptr puede incrementarse y
	   compararse con el valor c.
					
// Recorrer la memoria hasta el límite n	
	while (i < n)
	{
		if (*ptr == (char)c)   // Si se encuentra el byte buscado c

	El operador de desreferencia * se usa para acceder al contenido del puntero 
	ptr, que ahora es de tipo const char*. Convertimos c a char para asegurarnos
 	de que la comparación sea válida, ya que c es un entero y puede tener un 
	rango más amplio que un char.
		
		{
			return ((void *)ptr);  // Devolver un puntero al byte encontrado
		Dado que ptr es de tipo const char*, debemos convertirlo a void* antes
		 de retornarlo. Esto asegura que la función cumple con su prototipo y 
		 puede ser usada en contextos donde se espera un puntero genérico.
		}
		ptr++;
		i++;
	}
	return (NULL);  // Devuelve NULL si el byte buscado no se encuentra en
					// la memoria
}
*/