/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 10:03:48 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:59:39 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			count++;
			in_word = 1;
		}
		else if (*s == c)
		{
			in_word = 0;
		}
		s++;
	}
	return (count);
}

static char	*next_word(char const **s, char c)
{
	const char	*word_start;
	const char	*word_end;
	char		*new_word;

	word_start = *s;
	while (*word_start == c)
		word_start++;
	if (*word_start == '\0')
		return (NULL);
	word_end = word_start;
	while (*word_end != c)
		word_end++;
	if (word_end == word_start)
		return (NULL);
	new_word = ft_substr(word_start, 0, word_end - word_start);
	if (!new_word)
		return (NULL);
	*s = word_end;
	return (new_word);
}

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		num_words;
	int		i;

	if (!s)
		return (NULL);
	num_words = count_words(s, c);
	result = (char **)malloc((num_words + 1) * sizeof(char *));
	if (!result)
		return (NULL);
	i = 0;
	while (i < num_words)
	{
		result[i] = next_word(&s, c);
		if (!result[i])
		{
			while (i--)
				free(result[i]);
			free(result);
			return (NULL);
		}
		i++;
	}
	result[i] = NULL;
	return (result);
}

/* 
int	main(void)
{
	char const	*s = "Hello Maryann this is a test again";
	char		c;
	char		**result;
	int			i;

	i = 0;
	c = ' ';
	result = ft_split(s, c);
	if (result != NULL)
	{
		while (result[i] != NULL)
		{
			printf("Palabra %d: %s\n", i + 1, result[i]);
			free(result[i]);
			i++;
		}
		free(result);
	}
	else
		printf("Error: No se pudo dividir la cadena.\n");
	return (0);
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

// FUNCIONES AUTORIZADAS. malloc, free

// Divide una cadena en un número máximo de subcadenas en función
// de los caracteres de delimitación especificados.

/*

static int count_words(char const *s, char c)

Esta función llamada count_words cuenta el número de palabras en 
una cadena de caracteres s, donde las palabras están separadas por 
 un carácter delimitador c.

{
	int count;      // Contador de palabras
	int in_word;    // Flag para indicar si estamos dentro de 
						una palabra

	count = 0;      // Inicializamos el contador de palabras a 0
	in_word = 0;    // Inicializamos el flag a 0, indicando que
					 no estamos dentro de una palabra
					 flag, actua como interruptor, encendido 
					 (verdadero) o apagado (falso)

	// Iteramos sobre la cadena de caracteres hasta llegar al final
	while (*s)
	{
		// Si el caracter actual no es el delimitador y no estamos
			 dentro de una palabra
		if (*s != c && !in_word)
		{
			count++;    // Incrementamos el contador de palabras
			in_word = 1; // Cambiamos el flag para indicar que 
							estamos dentro de una palabra
		}
		// Si el caracter actual es el delimitador
		else if (*s == c)
		{
			in_word = 0; // Cambiamos el flag para indicar que
							 no estamos dentro de una palabra
		}
		s++; // Movemos el puntero al siguiente caracter
	}
	return (count); // Retornamos el contador de palabras
}

static char *next_word(char const **s, char c)

Esta función llamada next_word encuentra la próxima palabra en una
 cadena de caracteres s, donde las palabras están separadas por 
 un carácter delimitador c
{
	const char *word_start; // Puntero al inicio de la palabra
	const char *word_end;   // Puntero al final de la palabra
	char *new_word;         // Puntero a la nueva palabra

	word_start = *s; // Inicializamos el puntero al inicio de la 
						palabra
	// Avanzamos hasta encontrar el inicio de la siguiente palabra
	 o el final de la cadena
	while (*word_start == c)
		word_start++;
	word_end = word_start; // El fin de la palabra comienza en el
							 inicio
	// Avanzamos hasta encontrar el final de la palabra o el final
		 de la cadena
	while (*word_end != c)
		word_end++;
	// Si no hay caracteres entre word_start y word_end, retornamos
		 NULL
	if (word_end == word_start)
		return (NULL);
	// Creamos una nueva palabra usando la función ft_substr
	new_word = ft_substr(word_start, 0, word_end - word_start);
	if (!new_word) // Si no se pudo asignar memoria para la nueva
					 palabra, retornamos NULL
		return (NULL);
	*s = word_end; // Actualizamos el puntero s para que apunte
					 al final de la palabra procesada
	return (new_word); // Retornamos la nueva palabra
}

char **ft_split(char const *s, char c)

Esta función ft_split, divide una cadena de caracteres
 s en palabras separadas por un carácter delimitador c
{
	char **result;  // Puntero a un array de punteros que 
						contendrá las palabras divididas
	int num_words;  // Número de palabras en la cadena
	int i;          // Índice para recorrer el array de palabras

	if (!s) // Si la cadena es NULL, retornamos NULL
		return (NULL);
	num_words = count_words(s, c); // Contamos el número de 
									palabras en la cadena
	// Asignamos memoria para el array de palabras más un 
	elemento adicional para el marcador de fin NULL
	result = (char **)malloc((num_words + 1) * sizeof(char *));
	if (!result) // Si no se pudo asignar memoria, retornamos NULL
		return (NULL);
	i = 0; // Inicializamos el índice a 0
	// Iteramos para dividir la cadena en palabras y almacenarlas
	 en el array resultante
	while (i < num_words)
	{
		result[i] = next_word(&s, c); // Obtenemos la siguiente 
							palabra y la almacenamos en el array
		if (!result[i]) // Si no se pudo obtener una palabra, 
					liberamos la memoria asignada y retornamos NULL
		{
			while (i--) // Liberamos la memoria asignada para las 
						palabras previamente almacenadas
				free(result[i]);
			free(result); // Liberamos la memoria asignada para 
							el array de palabras
			return (NULL); // Retornamos NULL
		}
		i++; // Incrementamos el índice
	}
	result[i] = NULL; // Establecemos el marcador de fin NULL en
						la última posición del array
	return (result); // Retornamos el array de palabras
						divididas
}
*/
/* EJEMPLO
. Función count_words
Descripción:
Esta función cuenta el número de palabras en una cadena s, utilizando el carácter
 c como delimitador.

Código:
c
Copy code
static int	count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			count++;
			in_word = 1;
		}
		else if (*s == c)
		{
			in_word = 0;
		}
		s++;
	}
	return (count);
}
Ejemplo y Explicación Paso a Paso:
Supongamos que s = "hello world this is C" y c = ' ' (espacio).

Inicializamos count = 0 y in_word = 0.
Empezamos a iterar sobre s:
s = "hello world this is C"
*s = 'h' (no es un espacio y in_word es 0):
Incrementamos count a 1.
Establecemos in_word a 1.
Continuamos iterando mientras *s no sea espacio:
*s = 'e', *s = 'l', *s = 'l', *s = 'o'
*s = ' ' (es un espacio):
Establecemos in_word a 0.
Repetimos el proceso para las siguientes palabras:
*s = 'w' (no es un espacio y in_word es 0):
Incrementamos count a 2.
Establecemos in_word a 1.
*s = 'o', *s = 'r', *s = 'l', *s = 'd', *s = ' '
Establecemos in_word a 0.
*s = 't' (no es un espacio y in_word es 0):
Incrementamos count a 3.
Establecemos in_word a 1.
*s = 'h', *s = 'i', *s = 's', *s = ' '
Establecemos in_word a 0.
*s = 'i' (no es un espacio y in_word es 0):
Incrementamos count a 4.
Establecemos in_word a 1.
*s = 's', *s = ' '
Establecemos in_word a 0.
*s = 'C' (no es un espacio y in_word es 0):
Incrementamos count a 5.
Establecemos in_word a 1.
Al final del bucle, count será 5, indicando que hay 5 palabras en la cadena.

2. Función next_word
Descripción:
Esta función encuentra la siguiente palabra en la cadena s, utilizando el
 carácter c como delimitador, y devuelve una nueva cadena con esa palabra.

Código:
c
Copy code
static char	*next_word(char const **s, char c)
{
	const char	*word_start;
	const char	*word_end;
	char		*new_word;

	word_start = *s;
	while (*word_start == c)
		word_start++;
	if (*word_start == '\0')
		return (NULL);
	word_end = word_start;
	while (*word_end != c && *word_end != '\0')
		word_end++;
	if (word_end == word_start)
		return (NULL);
	new_word = ft_substr(word_start, 0, word_end - word_start);
	if (!new_word)
		return (NULL);
	*s = word_end;
	return (new_word);
}
Ejemplo y Explicación Paso a Paso:
Supongamos que s = "hello world this is C" y c = ' ' (espacio).

1. Inicializar word_start

word_start = *s;
word_start apunta al primer carácter de s.
En este ejemplo, word_start apunta a 'h' en "hello world this is C".

2. Saltar los delimitadores iniciales
while (*word_start == c)
	word_start++;
Este bucle avanza word_start hasta que encuentra un carácter que no es el 
delimitador c. el bucle verifica si hay caracteres delimitadores al principio y 
los salta, pero en este caso, como no hay delimitadores iniciales, word_start no 
avanza.
En nuestro ejemplo, word_start ya apunta a 'h', que no es un espacio, por lo que
 no avanza y sigue apuntando a 'h'.
 
3. Comprobar si hemos llegado al final de la cadena
if (*word_start == '\0')
	return (NULL);
Si word_start apunta al carácter nulo '\0', significa que no hay más palabras en 
la cadena, por lo que la función retorna NULL.
En nuestro ejemplo, word_start no apunta a '\0', así que seguimos.

4. Inicializar word_end
word_end = word_start;
word_end se inicializa para que apunte al mismo lugar que word_start, es decir, 
al inicio de la palabra encontrada.
En nuestro ejemplo, word_end también apunta a 'h'.

5. Encontrar el final de la palabra
while (*word_end != c && *word_end != '\0')
	word_end++;
Este bucle avanza word_end hasta que encuentra el delimitador c o el final de la
 cadena '\0'.
Para s = "hello world this is C", word_end avanzará sobre 'h', 'e', 'l', 
'l', 'o' y luego apuntará al espacio después de "hello".

6. Comprobar si la palabra está vacía
if (word_end == word_start)
	return (NULL);
Si word_end no ha avanzado (es decir, word_end es igual a word_start), entonces 
no se encontró una palabra, por lo que la función retorna NULL.
En nuestro ejemplo, word_end ha avanzado, así que seguimos.

7. Extraer la palabra
new_word = ft_substr(word_start, 0, word_end - word_start);
ft_substr crea una nueva cadena que contiene los caracteres desde word_start
 hasta word_end.
word_end - word_start calcula la longitud de la palabra.
En nuestro ejemplo, new_word será "hello".

8. Comprobar si la extracción falló

if (!new_word)
	return (NULL);
Si ft_substr falla (por ejemplo, por falta de memoria), new_word será NULL, por 
lo que la función retorna NULL.
En nuestro ejemplo, new_word no es NULL, así que seguimos.

9. Actualizar el puntero s
*s = word_end;
Actualizamos *s para que apunte al final de la palabra encontrada, lo cual es
 útil para encontrar la siguiente palabra en la cadena en llamadas sucesivas 
 a next word.
En nuestro ejemplo, *s ahora apuntará al espacio después de "hello" en " world 
this is C".

10. Retornar la nueva palabra
return (new_word);
Finalmente, retornamos la nueva palabra encontrada.
En nuestro ejemplo, retornamos "hello".
Resumen Completo del Proceso
Inicialización: word_start apunta al primer carácter de s, word_end se 
inicializa igual que word_start.
Saltar delimitadores: Si hay delimitadores al principio, los saltamos.
Verificar fin de cadena: Si word_start llega a '\0', no hay más palabras.


3. FUNCION SPLIT
Descripción:
Esta función divide la cadena s en una matriz de cadenas, utilizando el carácter
 c como delimitador.

a función ft_split toma una cadena s y un delimitador c, y devuelve un arreglo de
 cadenas (array de strings), donde cada elemento es una palabra separada por el 
 delimitador c en la cadena original.

Código de la Función
char **ft_split(char const *s, char c)
{
    char    **result;
    int     num_words;
    int     i;

    if (!s)
        return (NULL);
    num_words = count_words(s, c);
    result = (char **)malloc((num_words + 1) * sizeof(char *));
    if (!result)
        return (NULL);
    i = 0;
    while (i < num_words)
    {
        result[i] = next_word(&s, c);
        if (!result[i])
        {
            while (i--)
                free(result[i]);
            free(result);
            return (NULL);
        }
        i++;
    }
    result[i] = NULL;
    return (result);
}
Explicación Paso a Paso
1. Comprobar si s es NULL
if (!s)
    return (NULL);
Si la cadena de entrada s es NULL, la función retorna NULL inmediatamente porque 
no hay nada que dividir.

2. Contar el número de palabras
num_words = count_words(s, c);
La función count_words cuenta cuántas palabras hay en la cadena s usando el 
delimitador c.
Esto es necesario para saber cuántos elementos tendrá el arreglo de cadenas
 result.

3. Asignar memoria para el resultado
result = (char **)malloc((num_words + 1) * sizeof(char *));
Se asigna memoria para un arreglo de punteros a caracteres (char *), con espacio
 para num_words palabras más uno adicional para el puntero nulo final.
Si num_words es 5, se asigna espacio para 6 punteros (num_words + 1).

4. Comprobar si la asignación fue exitosa
if (!result)
    return (NULL);
Si malloc no pudo asignar la memoria necesaria, retorna NULL.

5. Inicializar el índice
i = 0;
Se inicializa el índice i para iterar a través de las palabras.

6. Extraer palabras y llenarlas en result
while (i < num_words)
{
    result[i] = next_word(&s, c);
    if (!result[i])
    {
        while (i--)
            free(result[i]);
        free(result);
        return (NULL);
    }
    i++;
}
Este bucle se ejecuta num_words veces.
En cada iteración, next_word se llama para obtener la siguiente palabra de la 
cadena s.
Si next_word devuelve NULL (indicando un error en la asignación de memoria para 
una palabra), se liberan todas las palabras previamente asignadas y result antes 
de retornar NULL.

7. Añadir un puntero nulo al final del arreglo
result[i] = NULL;
Se asigna NULL al último elemento del arreglo result para marcar el final del 
arreglo de cadenas.

8. Retornar el resultado
return (result);
Se retorna el arreglo de cadenas result.
Ejemplo Paso a Paso
Supongamos que s = "hello world this is C" y c = ' '.

Paso 1: Comprobar si s es NULL
s no es NULL, así que seguimos.
Paso 2: Contar el número de palabras
count_words(s, c) retorna 5 (las palabras son "hello", "world", "this", 
"is", "C").
Paso 3: Asignar memoria para result
Se asigna memoria para un arreglo de 6 punteros (5 + 1).
Paso 4: Comprobar si la asignación fue exitosa
La asignación fue exitosa, así que seguimos.
Paso 5: Inicializar el índice
i se inicializa a 0.
Paso 6: Extraer palabras y llenarlas en result
Primera Iteración (i = 0):
next_word(&s, c) retorna "hello".
result[0] se asigna a "hello".
Segunda Iteración (i = 1):
next_word(&s, c) retorna "world".
result[1] se asigna a "world".
Tercera Iteración (i = 2):
next_word(&s, c) retorna "this".
result[2] se asigna a "this".
Cuarta Iteración (i = 3):
next_word(&s, c) retorna "is".
result[3] se asigna a "is".
Quinta Iteración (i = 4):
next_word(&s, c) retorna "C".
result[4] se asigna a "C".
Paso 7: Añadir un puntero nulo al final del arreglo
result[5] se asigna a NULL para marcar el final del arreglo.
Paso 8: Retornar el resultado
La función retorna el arreglo result.
Resultado Final
El arreglo result contendrá:

result[0] = "hello"
result[1] = "world"
result[2] = "this"
result[3] = "is"
result[4] = "C"
result[5] = NULL
Este es el proceso detallado que sigue la función ft_split para dividir una
 cadena en palabras usando un delimitador. */
