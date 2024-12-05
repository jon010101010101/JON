/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/08 13:11:45 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/25 10:04:51 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	while (n > 0 && *s1 != '\0' && *s2 != '\0')
	{
		if (*s1 != *s2)
		{
			return ((unsigned char)*s1 - (unsigned char)*s2);
		}
		s1++;
		s2++;
		n--;
	}
	if (n == 0)
	{
		return (0);
	}
	return ((unsigned char)*s1 - (unsigned char)*s2);
}

int main(void)
{
	char str1[] = "JON";
	char str2[] = "JONOSOYJON";
	size_t	size;

	size = 3;

	printf("Comparando '%s' y '%s': %d\n", str1, str2, ft_strncmp(str1, str2, size));

	return (0);
}

// Compara dos cadenas de ccaracters hasta un máximo número
// de caracteres espeficicados

/* int ft_strncmp(char *s1, char *s2, unsigned int n)
{
	// Comenzamos un bucle que se ejecuta mientras queden caracteres por comparar
	(n > 0) y no hayamos llegado al final de ninguna de las dos cadenas
	while (n > 0 && *s1 != '\0' && *s2 != '\0')
	Se ejecuta mientras n sea mayor que 0 y no se haya alcanzado el final de 
	ninguna de las cadenas (*s1 != '\0' y *s2 != '\0').
		{
		// Si los caracteres actuales de s1 y s2 no son iguales,
		// devolvemos la diferencia entre ellos
		if (*s1 != *s2)
		{
			return ((unsigned char)*s1 - (unsigned char)*s2);
			
			Se convierte los caracteres a unsigned char antes de hacer la resta 
			en la expresión return ((unsigned char)*s1 - (unsigned char)*s2); es 
			para asegurar una comparación correcta de los valores de los 
			caracteres, no tengan valores negativos.
		}
		// Avanzamos al siguiente carácter en ambas cadenas
		s1++;
		s2++;
		// Decrementamos el contador de caracteres por comparar
		n--;
	}
	// Si n llega a cero, significa que hemos comparado los primeros n caracteres
	// y todos son iguales, así que devolvemos 0
	if (n == 0)
	{
		return (0);
	}
	// Si salimos del bucle porque llegamos al final de una de las cadenas,
	// devolvemos la diferencia entre los caracteres actuales de s1 y s2
	return ((unsigned char)*s1 - (unsigned char)*s2);
} */