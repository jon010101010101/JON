/*Assignment name  : ft_split
Expected files   : ft_split.c
Allowed functions: malloc
--------------------------------------------------------------------------------
Write a function that takes a string, splits it into words, and returns them as
a NULL-terminated array of strings.
A "word" is defined as a part of a string delimited either by spaces/tabs/new
lines, or by the start/end of the string.
Your function must be declared as follows:
char    **ft_split(char *str);
--------------------------------------------------------------------------------
Escribe una función que tome una cadena, la divida en palabras y las devuelva como
una matriz de cadenas terminada en NULL.
Una "palabra" se define como parte de una cadena delimitada por espacios/tabulaciones/nueva
líneas, o por el inicio/final de la cadena.
Su función debe declararse de la siguiente manera:
char **ft_split(char *str);*/

/* ANA OK */




/* COMENTARIOS ANA */

/* #include <unistd.h>   // Incluye las definiciones estándar de POSIX, aunque no se usan en este código
#include <stdio.h>    // Incluye funciones para la entrada/salida estándar, como printf
#include <stdlib.h>   // Incluye funciones estándar como malloc y free para manejo de memoria dinámica

// Función que copia una cadena de caracteres desde str2 hacia str1 hasta un máximo de n caracteres
char *ft_strcopy(char *str1, char *str2, int n)
{
    int i = 0;  // Inicializamos un índice i para iterar sobre los caracteres

    // Copiamos los caracteres de str2 a str1, hasta que hayamos copiado n caracteres o lleguemos al final de str2
    while (i < n && str2[i])
    {
        str1[i] = str2[i];  // Copiamos el carácter actual de str2 a str1
        i++;  // Avanzamos al siguiente índice
    }
    str1[i] = '\0';  // Añadimos el carácter nulo al final de str1 para indicar el fin de la cadena
    return (str1);  // Retornamos el puntero a la cadena copiada
}

// Función que verifica si un carácter es un espacio en blanco (espacio, tabulación o nueva línea)
int ft_is_space(char c)
{
    // Retorna 1 si el carácter es un espacio en blanco, 0 si no lo es
    return (c == ' ' || c == '\t' || c == '\n');
}

// Función que divide una cadena en palabras, utilizando espacios como delimitadores
char **ft_split(char *str)
{
    int i = 0;  // Índice para recorrer la cadena original
    int j = 0;  // Índice auxiliar para marcar el inicio de una palabra
    int words = 0;  // Contador del número de palabras encontradas
    int k = 0;  // Índice para recorrer el arreglo de palabras (out)

    // Primero, contamos cuántas palabras hay en la cadena
    while (str[i])
    {
        // Saltamos los espacios en blanco
        while (str[i] && ft_is_space(str[i]))
        {
            i++;
        }
        // Si encontramos un carácter que no es espacio, contamos una palabra
        if (str[i])
        {
            words++;
        }
        // Continuamos avanzando hasta el final de la palabra
        while (str[i] && !ft_is_space(str[i]))
        {
            i++;
        }
    }

    // Asignamos memoria para un arreglo de punteros a cadenas, con espacio para 'words' palabras más un NULL final
    char **out = (char **)malloc(sizeof(char *) * (words + 1));
    if (!out)
    {
        return (NULL);  // Si falla la asignación de memoria, retornamos NULL
    }

    // Reiniciamos el índice para recorrer la cadena de nuevo y extraer las palabras
    i = 0;
    while (str[i])
    {
        // Saltamos los espacios en blanco nuevamente
        while (str[i] && ft_is_space(str[i]))
        {
            i++;
        }
        j = i;  // Marcamos el inicio de la palabra
        // Continuamos avanzando hasta el final de la palabra
        while (str[i] && !ft_is_space(str[i]))
        {
            i++;
        }
        // Si se encontró una palabra (i > j), la copiamos al arreglo 'out'
        if (i > j)
        {
            out[k] = (char *)malloc(sizeof(char) * (i - j + 1));  // Asignamos memoria para la palabra
            ft_strcopy(out[k++], &str[j], i - j);  // Copiamos la palabra desde 'str' hacia 'out[k]'
        }
    }
    out[k] = NULL;  // Añadimos un puntero NULL al final del arreglo para marcar su terminación

    return (out);  // Retornamos el arreglo de punteros a palabras
}

// Función principal que prueba el comportamiento de ft_split
int main(void)
{
    // Llamamos a ft_split con una cadena y almacenamos el resultado en el arreglo de cadenas 'frase'
    char **frase = ft_split("a ver si apruebo de una vez");
    int i = 0;  // Inicializamos un índice para recorrer el arreglo de palabras

    // Imprimimos cada palabra en el arreglo 'frase' junto con su índice
    while (frase[i])
    {
        printf("%d: %s\n", i, frase[i]);  // Imprimimos el índice y la palabra correspondiente
        i++;
    }

    // Aquí podrías añadir código para liberar la memoria asignada (no incluido)
    return (0);  // Retornamos 0 para indicar que el programa terminó correctamente
} */

/*JON BUENA*/

/* #include <stdlib.h>

int is_delimiter(char c)
{
    return (c == ' ' || c == '\t' || c == '\n');
}

int count_words(char *str)
{
    int count = 0;

    while (*str)
    {
        while (*str && is_delimiter(*str))
            str++;
        if (*str && !is_delimiter(*str))
        {
            count++;
            while (*str && !is_delimiter(*str))
                str++;
        }
    }
    return (count);
}

char *create_word(char *start, char *end)
{
    int len = end - start;
    char *word = (char *)malloc(sizeof(char) * (len + 1));
    int i = 0;

    while (start < end)
        word[i++] = *start++;
    word[i] = '\0';

    return (word);
}

char **ft_split(char *str)
{
    char **result;
    int words = count_words(str);
    int i = 0;

    result = (char **)malloc(sizeof(char *) * (words + 1));
    if (!result)
        return (NULL);

    while (*str)
    {
        while (*str && is_delimiter(*str))
            str++;
        if (*str && !is_delimiter(*str))
        {
            char *start = str;
            while (*str && !is_delimiter(*str))
                str++;
            result[i++] = create_word(start, str);
        }
    }
    result[i] = NULL;

    return (result);
}


#include <stdio.h>
#include <stdlib.h>

int main()
{
    char **words;
    char str[] = "  This is \ta test\nstring ";

    words = ft_split(str);

    int i = 0;
    while (words[i])
    {
        printf("Word %d: %s\n", i, words[i]);
        free(words[i]);  // Free each word after use
        i++;
    }
    free(words);  // Free the array of words

    return (0);
} */
/* COMENTARIOS */

/* #include <stdlib.h>  // Incluimos la biblioteca estándar para manejo de memoria dinámica

// Función que verifica si un carácter es un delimitador (espacio, tabulación o nueva línea)
int is_delimiter(char c)
{
    // Retorna 1 si el carácter es un delimitador, de lo contrario retorna 0
    return (c == ' ' || c == '\t' || c == '\n');
}

// Función que cuenta el número de palabras en una cadena
int count_words(char *str)
{
    int count = 0;  // Inicializamos el contador de palabras en 0

    // Recorremos la cadena carácter por carácter
    while (*str)
    {
        // Saltamos los delimitadores iniciales (espacios, tabulaciones, etc.)
        while (*str && is_delimiter(*str))
            str++;  // Avanzamos al siguiente carácter

        // Si encontramos un carácter que no es un delimitador
        if (*str && !is_delimiter(*str))
        {
            count++;  // Incrementamos el contador de palabras

            // Continuamos avanzando hasta encontrar el final de la palabra
            while (*str && !is_delimiter(*str))
                str++;  // Avanzamos al siguiente carácter
        }
    }
    // Retornamos el número total de palabras contadas
    return (count);
}

// Función que crea una palabra copiando caracteres desde 'start' hasta 'end'
char *create_word(char *start, char *end)
{
    int len = end - start;  // Calculamos la longitud de la palabra
    char *word = (char *)malloc(sizeof(char) * (len + 1));  // Asignamos memoria para la palabra (+1 para '\0')
    int i = 0;  // Inicializamos el índice para llenar la nueva palabra

    // Copiamos los caracteres desde 'start' hasta 'end' en la nueva palabra
    while (start < end)
        word[i++] = *start++;  // Copiamos y avanzamos tanto en 'word' como en 'start'

    word[i] = '\0';  // Añadimos el carácter nulo para terminar la cadena
    return (word);  // Retornamos el puntero a la nueva palabra
}

// Función que divide una cadena en palabras, utilizando delimitadores
char **ft_split(char *str)
{
    char **result;  // Declaramos un puntero para el arreglo que contendrá las palabras
    int words = count_words(str);  // Contamos el número de palabras en la cadena
    int i = 0;  // Inicializamos el índice para llenar el arreglo 'result'

    // Asignamos memoria para un arreglo de punteros a cadenas (más uno para el NULL final)
    result = (char **)malloc(sizeof(char *) * (words + 1));
    if (!result)
        return (NULL);  // Si falla la asignación de memoria, retornamos NULL

    // Recorremos la cadena original 'str'
    while (*str)
    {
        // Saltamos los delimitadores iniciales
        while (*str && is_delimiter(*str))
            str++;  // Avanzamos al siguiente carácter

        // Si encontramos una palabra (un carácter que no es delimitador)
        if (*str && !is_delimiter(*str))
        {
            char *start = str;  // Marcamos el inicio de la palabra
            // Continuamos avanzando hasta el final de la palabra
            while (*str && !is_delimiter(*str))
                str++;  // Avanzamos al siguiente carácter

            // Creamos la palabra y la almacenamos en 'result[i]'
            result[i++] = create_word(start, str);
        }
    }
    result[i] = NULL;  // Añadimos un puntero NULL al final del arreglo para marcar su terminación

    return (result);  // Retornamos el arreglo de punteros a palabras
} */

#include <stdio.h>
#include <ctype.h>

#define MAX_CHARS 4096  // Tamaño máximo de la cadena
#define MAX_WORDS 1024  // Suponemos un máximo de 1024 palabras

// Función para dividir la cadena
char **ft_split(char *str)
{
    static char words_array[MAX_WORDS][MAX_CHARS];  // Array para almacenar palabras
    static char *words[MAX_WORDS + 1];  // Array de punteros a palabras
    int i = 0, j = 0, k = 0;

    // Procesar cada carácter de la cadena
    while (str[i])
    {
        // Ignorar los espacios al principio
        while (str[i] && isspace(str[i]))
        {
            i++;
        }

        // Si llegamos al final de la cadena, salimos
        if (!str[i])
        {
            break;
        }

        // Copiar la palabra al array
        k = 0;
        while (str[i] && !isspace(str[i]) && k < MAX_CHARS - 1)
        {
            words_array[j][k] = str[i];
            k++;
            i++;
        }

        // Terminar la palabra con el carácter nulo
        words_array[j][k] = '\0';

        // Guardar el puntero a la palabra en el array de punteros
        words[j] = words_array[j];
        j++;

        // Asegurarnos de no superar el número máximo de palabras
        if (j >= MAX_WORDS) {
            break;
        }
    }

    words[j] = NULL;  // Terminar el array de punteros con NULL
    return words;
}

// Ejemplo de uso
int main()
{
    char str[MAX_CHARS] = "Hola, esta es una prueba\ncon\tvarias palabras.";
    char **words = ft_split(str);
    int i = 0;

    // Imprimir cada palabra separada
    while (words[i])
    {
        printf("Palabra %d: %s\n", i, words[i]);
        i++;
    }

    return (0);
}




/*SANDRA OK*/

/* #include <stdlib.h>

char *ft_strncopy(char *s1, char *s2, int n)
{
	int i = -1;
	while (++i < n && s2[i])
		s1[i] = s2[i];
	s1[i] = '\0';
	return (s1);
}

int is_space(char ch)
{
	return(ch == ' ' || ch == '\t' || ch == '\n');
}

int number_words(char *str)
{
	int i = 0;
	int number = 0;

	while (str[i])
	{
		while (str[i] && is_space(str[i]))
			i++;
		if (str[i])
			number++;
		while (str[i] && !is_space(str[i]))
			i++;
	}
	return (number);
}
char	**ft_split(char *str)
{
	if (!str)
		return (NULL);
	int i = 0;
	int k = 0;
	int initword;
	int n_words = number_words(str);
	char **split;
	split = (char **)malloc(sizeof(char *) * (n_words + 1));
	if (!split)
		return (NULL);
	while (str[i])
	{
		while (str[i] && is_space(str[i]))
			i++;
		initword = i;
		while (str[i] && !is_space(str[i]))
			i++;
		if (initword < i)
		{
			split[k] = (char *)malloc(sizeof(char) * ((i - initword) + 1));
			ft_strncopy(split[k++], &str[initword], i - initword);
		}
	}
	split[k] = NULL;
	return(split);
}

#include <stdio.h>
int	main()
{
 	char **frase = ft_split("hola que tal");
 	int i = 0;

 	while (frase[i])
 	{
 		printf("string %d: %s\n", i, frase[i]);
 		i++;
 	}
 	return (0);
} */



