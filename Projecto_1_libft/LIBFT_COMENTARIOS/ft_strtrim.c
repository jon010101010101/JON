/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/20 10:48:13 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:43:07 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	int		len;
	int		start;
	int		end;
	int		result_len;
	char	*result;

	len = ft_strlen(s1);
	start = 0;
	end = len - 1;
	while (s1[start] != '\0' && ft_strchr(set, s1[start]) != NULL)
		start++;
	while (s1[start] != '\0' && ft_strchr(set, s1[end]) != NULL)
		end--;
	result_len = end - start + 1;
	result = (char *)malloc((result_len + 1) * sizeof(char));
	if (result == NULL)
		return (NULL);
	if (result != NULL)
		ft_strlcpy(result, s1 + start, result_len + 1);
	result[result_len] = '\0';
	return (result);
}

/* int main(void)
{
	char	*s1;
	char	*set;

	s1 = "  Hello, world!  ";
	set = " ";

	printf("La string resutante es: %s\n", ft_strtrim(s1,set));
	return (0);
} */

//DESCRIPCION. Elimina todos los caracteres de la string ’set’ 
//desde el principio y desde el final de ’s1’, hasta encontrar 
// un caracter no perteneciente a ’set’. La string resultante
//se devuelve con una reserva de malloc(3)

// VALOR DEVUELTO. La string recortada. NULL si falla la reserva
// de memoria.

// PARAMETROS. 
// s1: La string que debe ser recortada.
// set: Los caracteres a eliminar de la string.

// La función ft_strtrim toma dos cadenas de caracteres (s1 y set)
// y devuelve una nueva cadena que es una copia de s1 con los 
// caracteres que aparecen en set eliminados del principio y del final
// de la cadena.

/* 
// Función para extraer una subcadena de una cadena dada//
char *ft_substr(char const *s, unsigned int start, size_t len)
{
	char *str;         // Puntero para almacenar la nueva subcadena
	size_t size_s;     // Variable para almacenar el tamaño de la cadena s
	size_t i;          // Variable de iteración

	// Verificamos si la cadena de entrada s es NULL
	if (s == NULL)
		return (NULL); // Si es NULL, devolvemos NULL

	// Calculamos el tamaño de la cadena s usando la función ft_strlen
	size_s = ft_strlen((char *)s);

	// Verificamos si el índice de inicio start está fuera de los límites de
	 s o si la longitud len es 0
	if (start >= size_s || len == 0)
		return (ft_strdup("")); // Si es así, devolvemos una cadena vacía

	// Ajustamos la longitud len si es necesario para asegurarnos de que no
	sobrepase el tamaño de s desde start
	if (start + len > size_s)
		len = size_s - start;

	// Asignamos memoria para la nueva subcadena str, más uno adicional para
	 el carácter nulo '\0'
	str = malloc(len + 1);
	// Verificamos si la asignación de memoria fue exitosa
	if (str == NULL)
		return (NULL); // Si falla, devolvemos NULL

	i = 0; // Inicializamos el índice i a 0
	// Copiamos len caracteres desde la posición start de s a str
	while (s[i] != '\0' && len > 0)
	{
		str[i] = s[start]; // Copiamos el carácter actual de s a la nueva 
		subcadena
		start++;           // Incrementamos el índice start para avanzar en s
		len--;             // Decrementamos la longitud restante
		i++;               // Incrementamos el índice i para avanzar en str
	}
	str[i] = '\0'; // Establecemos el último carácter de la nueva subcadena 
	como '\0' para terminarla
	return (str);  // Devolvemos la nueva subcadena str
}
 */

/* Inicialización:

s1 = " Hello, world! "
set = " "
len = ft_strlen(s1) = 17
start = 0
end = len - 1 = 16
Recortar caracteres desde el inicio:

Iteración 1:
s1[start] = ' ', ft_strchr(set, ' ') != NULL, incrementar start (start = 1)
Iteración 2:
s1[start] = ' ', ft_strchr(set, ' ') != NULL, incrementar start (start = 2)
Iteración 3:
s1[start] = 'H', ft_strchr(set, 'H') = NULL, salir del bucle.
Recortar caracteres desde el final:

Iteración 1:
s1[end] = ' ', ft_strchr(set, ' ') != NULL, decrementar end (end = 15)
Iteración 2:
s1[end] = ' ', ft_strchr(set, ' ') != NULL, decrementar end (end = 14)
Iteración 3:
s1[end] = '!', ft_strchr(set, '!') = NULL, salir del bucle.
Calcular la longitud del resultado y asignar memoria:

result_len = end - start + 1 = 14 - 2 + 1 = 13
Asignar memoria: result = (char *)malloc((result_len + 1) * sizeof(char))
Si result = NULL, retornar NULL
Copiar la subcadena recortada:

ft_strlcpy(result, s1 + start, result_len + 1)
Esto copiará "Hello, world!" a result.
Asegurarse de que la cadena terminada en nulo:

result[result_len] = '\0'
Retornar el resultado:

Retornar result
Resultado
En nuestro ejemplo, result apuntará a "Hello, world!" */