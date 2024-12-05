/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 11:27:38 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:52:40 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *big, const char *little, size_t len)
{
	size_t	little_len;
	size_t	i;

	if (*little == '\0')
		return ((char *) big);
	little_len = 0;
	while (little[little_len] != '\0')
		little_len++;
	while (*big != '\0' && len >= little_len)
	{
		i = 0;
		while (little[i] != '\0' && big[i] == little[i])
			i++;
		if (little[i] == '\0')
			return ((char *) big);
		big++;
		len--;
	}
	return (NULL);
}

/* int main()
{
	const char *big = "Hello, world!";
	const char *little = "world";
	size_t len = 12;

	char *result = ft_strnstr(big, little, len);

	if (result != NULL)
	{
		printf("Se encontró la subcadena '%s' en '%s'\n", little, big);
		printf("La subcadena comienza en la posición %ld\n", result - big);
	}
	else
	{
		printf("No se encontró la subcadena '%s' en '%s'\n", little, big);
	}
	return 0;
} */

/*La función ft_strnstr busca la primera aparición de la cadena little en la 
cadena big, pero solo hasta los primeros len caracteres de big. Si
 little es una cadena vacía, se devuelve big. Si needle no se encuentra 
 en los primeros len caracteres de big, se devuelve NULL. */

/* char *ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t needle_len;  // Longitud de la cadena 'needle'
	size_t i;           // Índice para iterar sobre 'needle'

	// Si 'needle' es una cadena vacía, devolvemos 'haystack'
	if (*needle == '\0')
		return ((char *)haystack);

		se retorna ((char *)haystack) en la función ft_strnstr es proporcionar 
		un puntero al comienzo de la primera ocurrencia de la subcadena needle
		dentro de haystack. Al hacer el casting a char *, aseguramos que el tipo
		de retorno coincide con el tipo esperado por la función.

	// Calculamos la longitud de 'needle'
	needle_len = 0;
	while (needle[needle_len] != '\0')
		needle_len++;

	// Iteramos sobre 'haystack' hasta que alcancemos el final de la cadena o 
		no queden suficientes caracteres para que 'needle' encaje
	while (*haystack != '\0' && len >= needle_len)
	{
		// Comenzamos a comparar 'needle' con la subcadena actual de 'haystack'
		i = 0;
		while (needle[i] != '\0' && haystack[i] == needle[i])
			i++;
		
		// Si hemos llegado al final de 'needle', significa que hemos encontrado 
		una coincidencia
		if (needle[i] == '\0')
			return ((char *)haystack);
		
		// Avanzamos el puntero de 'haystack' y decrementamos 'len'
		haystack++;
		len--;
	}

	// Si no encontramos 'needle' en 'haystack', devolvemos NULL
	return (NULL);
} */

/*  Inicialización y verificación de entrada vacía:

Verificación inicial de needle:

*needle = 'w', no es '\0', así que no retornamos haystack.
Calcular needle_len:

needle_len se incrementa mientras no lleguemos al final de needle.
needle_len = 5 (longitud de "world").
Primer bucle while:

*haystack = 'H', len = 12, needle_len = 5.
La condición *haystack != '\0' && len >= needle_len es verdadera.
Segundo bucle while (comparación carácter a carácter):

i = 0:
haystack[i] = 'H' y needle[i] = 'w' no coinciden, salir del bucle interno.
Avanzar haystack un carácter (haystack = "ello, world!"), decrementar len 
(len = 11).
Repetir proceso:

*haystack = 'e', len = 11.
i = 0:
haystack[i] = 'e' y needle[i] = 'w' no coinciden, salir del bucle interno.
Avanzar haystack un carácter (haystack = "llo, world!"), decrementar len 
(len = 10).
Continuar iterando:

Continuamos este proceso hasta haystack = " world!" y len = 6.
Coincidencia encontrada:

*haystack = 'w', len = 6.
i = 0:
haystack[i] = 'w' y needle[i] = 'w' coinciden, incrementar i.
haystack[i] = 'o' y needle[i] = 'o' coinciden, incrementar i.
haystack[i] = 'r' y needle[i] = 'r' coinciden, incrementar i.
haystack[i] = 'l' y needle[i] = 'l' coinciden, incrementar i.
haystack[i] = 'd' y needle[i] = 'd' coinciden, incrementar i.
needle[i] = '\0', coincidencia completa encontrada.
Retornar puntero a "world!" dentro de "Hello, world!". */