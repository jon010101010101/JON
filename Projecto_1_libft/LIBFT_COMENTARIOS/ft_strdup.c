/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 12:30:03 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:43:22 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *src)
{
	int		i;
	int		len;
	char	*dst;

	i = 0;
	len = 0;
	while (src[len] != '\0')
	{
		len++;
	}
	len++;
	dst = (char *)malloc(len * sizeof(char));
	if (dst == NULL)
		return (NULL);
	while (src[i] != '\0')
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (dst);
}

/* int main(void)
{
	const char *original = "Hola Manola!";
	char *duplicado = strdup(original);

	if (duplicado != NULL)
	{
		printf("Original: %s\n", original);
		printf("Duplicado: %s\n", duplicado);

		free(duplicado);
	}
	else
	{
		printf("Error: No se pudo duplicar la cadena.\n");
	}
	return 0;
} */

// Asigna la suficiente memoria dinamica para duplicar la cadena
// y vuelve el puntero a la bueva cadena.

/*
char *ft_strdup(const char *src)
{
    // Declaración de variables
    int i = 0; // Iterador para recorrer la cadena src
    int len = 0; // Variable para almacenar la longitud de la cadena src
    char *dst; // Puntero donde se almacenará la copia de src

    // Se recorre la cadena src para calcular su longitud, incrementando len 
		hasta encontrar el carácter nulo ('\0').
		
    while (src[len] != '\0')
	{
        len++; // Incrementar la longitud mientras no se alcance el carácter nulo
    }
    len++; // Se incrementa len una vez más para incluir el carácter nulo en la 
			longitud total.

    // Asignar memoria para la cadena de destino (copia)
    dst = (char *)malloc(len * sizeof(char));
    if (dst == NULL)
	{
        return (NULL); // Si no se puede asignar memoria, retornar NULL
    }

    // Copiar src en dst utilizando un bucle
    while (src[i] != '\0')
	{
        dst[i] = src[i]; // Copiar cada carácter de src en dst
        i++; // Avanzar al siguiente carácter
    }
    dst[i] = '\0'; // Agregar el carácter nulo al final de la cadena de destino

    // Retornar el puntero a la cadena de destino
    return (dst);
}

*/