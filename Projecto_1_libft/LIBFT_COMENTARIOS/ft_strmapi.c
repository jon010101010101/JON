/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/20 11:40:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:54:32 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*n_str;
	int		i;
	int		size_str;

	if (s == NULL)
		return (NULL);
	size_str = strlen(s);
	n_str = (char *) malloc ((size_str +1) * sizeof(char));
	if (n_str == NULL)
		return (NULL);
	i = 0;
	while (s[i] != '\0')
	{
		n_str[i] = f(i, s[i]);
		i++;
	}
	n_str[i] = '\0';
	return (n_str);
}

/* char ft_example_function(unsigned int i, char c)
{
		(void) i;
		if (c >= 'a' && c <= 'z')
			return (c -= 32);
		return (c);
}

int	main(void)
{
	char			*s;
	char			*n_str;
	
	s = "abcdefg";
	n_str = ft_strmapi(s, ft_example_function);
	printf("the string created after f is: %s\n", n_str);
	free (n_str);
	return (0);
}  */

/* esta puesto FUNCION pero habra que ponerle una funcion que haga algo
para poder probar si complica y ejecuta. Con Paco si funciona */

// DESCRIPCION. A cada carácter de la string ’s’, aplica la función 
// ’f’ dando como parámetros el índice de cada carácter dentro de ’s’
// y el propio carácter. Genera una nueva string con el resultado 
// del uso sucesivo de ’f’

// VALOR DEVUELTO. La string creada tras el correcto uso de ’f’ sobre
// cada carácter. NULL si falla la reserva de memoria.

// PARAMETROS. 
// s: La string que iterar.
// f: La función a aplicar sobre cada carácter.

// La función ft_strmapi en C toma una cadena de caracteres s y una
// función f como argumentos. La función f espera recibir dos argumentos:
// un índice sin signo (unsigned int) y un carácter (char). La función 
// ft_strmapi aplica la función f a cada carácter de la cadena s, pasando
// también el índice de ese carácter como primer argumento, y devuelve una 
// nueva cadena de caracteres que contiene los resultados de aplicar la 
// función f a cada carácter de la cadena original s

/* char *ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char *n_str;      // Puntero para almacenar la nueva cadena
	int i;            // Variable para iterar sobre la cadena s
	int size_str;     // Variable para almacenar el tamaño de la cadena s

	// Verificamos si la cadena de entrada s es NULL
	if (s == NULL)
		return (NULL);  // Si es NULL, devolvemos NULL

	// Calculamos el tamaño de la cadena s usando la función strlen
	size_str = strlen(s);

	// Asignamos memoria para la nueva cadena n_str, más uno adicional
	 para el carácter nulo '\0'
	n_str = (char *)malloc((size_str + 1) * sizeof(char));
	// Verificamos si la asignación de memoria fue exitosa
	if (n_str == NULL)
		return (NULL);  // Si falla, devolvemos NULL

	i = 0;  // Inicializamos el índice i a 0
	// Iteramos sobre cada carácter de la cadena s hasta llegar al carácter 
	nulo '\0'
	while (s[i] != '\0')
	{
		// Llamamos a la función f con el índice i y el carácter s[i] como
		 argumentos,
		// y almacenamos el resultado en n_str[i]
		n_str[i] = f(i, s[i]);
		i++;  // Incrementamos el índice para pasar al siguiente carácter de s
	}
	n_str[i] = '\0';  // Establecemos el último carácter de la nueva cadena 
	como '\0' para terminarla
	return (n_str);   // Devolvemos la nueva cadena n_str
} */