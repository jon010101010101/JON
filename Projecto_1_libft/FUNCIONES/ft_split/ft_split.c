/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/23 12:14:15 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/13 12:33:21 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"


/* 
int	main(void)
{
	
}
 */
// DESCRIPCION. Reserva (utilizando malloc(3)) un array de strings
// resultante de separar la string ’s’ en substrings utilizando el 
// caracter ’c’ como delimitador. El array debe terminar con un 
// puntero NULL.

// VALOR DEVUELTO. El array de nuevas strings resultante de la
// separación. NULL si falla la reserva de memoria.

// PARAMETROS. 
// s: La string a separar.
// c: El carácter delimitador

// FUNCIONES AUTOIRZADAS. malloc, free

// Divide una cadena en un número máximo de subcadenas en función
// de los caracteres de delimitación especificados.

/* static int count_words(char const *s, char c)
{
    int count = 0;     // Inicializamos el contador de palabras
    int in_word = 0;   // Flag para indicar si estamos dentro de una palabra

    // Iteramos sobre cada carácter de la cadena s
    while (*s)
    {
        // Si encontramos un carácter diferente de c y no estamos dentro
		 de una palabra
        if (*s != c && !in_word)
        {
            count++;    // Incrementamos el contador de palabras
            in_word = 1;  // Indicamos que estamos dentro de una palabra
        }
        // Si encontramos el carácter c, indicamos que estamos fuera
		 de una palabra
        else if (*s == c)
        {
            in_word = 0;
        }
        s++;  // Avanzamos al siguiente carácter en la cadena
    }
    return count;  // Devolvemos el número total de palabras contadas
}

static char *next_word(char const **s, char c)
{
    const char *word_start;  // Puntero al inicio de la próxima palabra
    const char *word_end;    // Puntero al final de la próxima palabra
    char *new_word;          // Puntero para almacenar la nueva palabra

    word_start = *s;  // Inicializamos word_start al puntero actual
    // Avanzamos word_start hasta el próximo carácter que no sea c
    while (*word_start && *word_start == c)
        word_start++;
    word_end = word_start;  // Inicializamos word_end a word_start
    // Avanzamos word_end hasta el próximo carácter c o el final de la cadena
    while (*word_end && *word_end != c)
        word_end++;
    // Si word_end y word_start coinciden, no hay palabra para extraer,
	 devolvemos NULL
    if (word_end == word_start)
        return NULL;
    // Usamos ft_substr para extraer la palabra entre word_start y word_end
    new_word = ft_substr(word_start, 0, word_end - word_start);
    // Si no se puede asignar memoria para new_word, devolvemos NULL
    if (!new_word)
        return NULL;
    *s = word_end;  // Actualizamos el puntero s al final de la palabra 
	encontrada
    return new_word;  // Devolvemos la nueva palabra extraída
}

char **ft_split(char const *s, char c)
{
    char **result;   // Array de punteros para almacenar las palabras
    int num_words;   // Número total de palabras en la cadena
    int i;           // Índice para iterar sobre las palabras

    if (!s)
        return NULL;  // Si la cadena de entrada es NULL, devolvemos NULL

    num_words = count_words(s, c);  // Contamos el número total de palabras
	 en la cadena
    // Asignamos memoria para el array de punteros result, más uno adicional
	 para el marcador de fin de cadena NULL
    result = (char **)malloc((num_words + 1) * sizeof(char *));
    if (!result)
        return NULL;  // Si no se puede asignar memoria, devolvemos NULL

    i = 0;  // Inicializamos el índice a 0
    // Iteramos sobre cada palabra en la cadena y las extraemos usando next_word
    while (i < num_words)
    {
        result[i] = next_word(&s, c);  // Extraemos la próxima palabra y la 
		almacenamos en result[i]
        // Si no se puede extraer la palabra, liberamos la memoria asignada
		previamente y devolvemos NULL
        if (!result[i])
        {
            while (i--)
                free(result[i]);
            free(result);
            return NULL;
        }
        i++;  // Incrementamos el índice para la próxima palabra
    }
    result[i] = NULL;  // Establecemos el último elemento de result en NULL
    return result;     // Devolvemos el array de palabras extraídas
} */