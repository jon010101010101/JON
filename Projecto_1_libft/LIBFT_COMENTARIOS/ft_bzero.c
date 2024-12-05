/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 13:07:51 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 16:58:10 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	char	*p;
	size_t	i;

	p = (char *)s;
	i = 0;
	while (i < n)
	{
		*p = '\0';
		p++;
		i++;
	}
}
/*
int main()
{
	char cadena[10] = "pepe";

	ft_bzero(cadena, sizeof(cadena)); 
	printf("Tamaño de la cadena: %lu\n", sizeof(cadena));
	printf("Contenido de la cadena: %s\n", cadena);

	return (0);
}
*/
// Pone a cero los primeros n bytes del área de bytes que comienza en s.

/*
void ft_bzero(void *s, size_t n)
{
    // Se declara un puntero de tipo char llamado p
    char *p;
    // Se declara una variable de tipo size_t llamada i para utilizarla 
	como iterador
    size_t i;

    // Se asigna a p la dirección de memoria inicial de s. Se castea para 
    convertir en char 
    p = (char *)s;
    // Se inicializa i a 0
    i = 0;

    // Se inicia un bucle while que se ejecutará mientras i sea menor que n
    while (i < n)
	{
        // Se asigna el carácter nulo ('\0') al valor apuntado por p
        *p = '\0';

        // Se incrementa el puntero p para apuntar al siguiente elemento
        p++;

        // Se incrementa el iterador i
        i++;
    }
}
Esta función establece todos los bytes de un bloque de memoria a cero.
**
** s: Puntero al inicio del bloque de memoria.
** n: Número de bytes a establecer a cero.
**
** Devuelve: Nada.
**
** Detalles de implementación:
** - Se utiliza un puntero 'p' para recorrer el bloque de memoria.
** - Se asigna el valor nulo ('\0') a cada byte en el bloque de memoria.
** - El bucle se repite 'n' veces para procesar todos los bytes.
**
** Nota: Esta función es eficiente y útil para limpiar bloques de memoria

*/