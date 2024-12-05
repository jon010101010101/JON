#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char *ft_strncpy(char *dest, const char *src, size_t n)
{
    size_t i;

    i = 0;
    while (i < n && src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
    return dest;
}

/*
LA FUNCION STRNCPY la puedes generar desde la ayuda:
man strncpy

char *
           strncpy(char *dest, const char *src, size_t n)
           {
               size_t i;

               for (i = 0; i < n && src[i] != '\0'; i++)
                   dest[i] = src[i];
               for ( ; i < n; i++)
                   dest[i] = '\0';

               return dest;
           }

TUNEALA añadiendo "ft_" y transformando los "for" en un simple while
*/

int ft_type_char(char c)          // Función para controlar que tipo de caracter es
{
    if ((c >= 9 && c <= 13)       // Si "c" es igual a cualquier espacio ascii
                                  //    9  '\t' (horizontal tab
                                  //    10 '\n' (new line)
                                  //    11 '\v' (vertical tab)
                                  //    12 '\f' (form feed)
                                  //    13 '\r' (carriage ret)
        || (c == 32))             // O si "c" es igual 32  ' ' SPACE
        return (0);               // Devuelvo 0
    else if (c >= 33 && c <= 126) // Si "c" es ascii printable ente 33 y 126
         return (1);              // Devuelvo 1
    else
        return (2);               //Devuelvo 2 (OJO 127 NO es printable)
}

int ft_count_words(char *str)
{
    int i;
    int words;

    i = 0;                                  // Contador para recorrer el argumento
    words = 0;                              // Contador para contar el numero de palabras
    while (str[i] != '\0')
    {
        while ((str[i] != '\0')             // Recorro el argumento mientras el carácter sea de tipo espacio y aumento el contador
            && (ft_type_char(str[i]) == 0))
            i++;
        if (ft_type_char(str[i]) == 1)      // Si el caracter es printable
            words++;                        // Aumento del contador de palabras
        while ((str[i] != '\0')             // Recorro el argumento mientras el carácter sea printable y aumento el contador
            && (ft_type_char(str[i]) == 1))
            i++;
    }
    return (words);                         // Devuelvo el número de palabras
}

char **ft_split(char *str)
{
    char    **split;
    int     init_word;
    int     i;
    int     j;

    i = 0;                                                                      // Contador para recorrer el argumento str
    j = 0;                                                                      // Contador para recorrer el array aplit
    init_word = 0;                                                              // Contador para controlar el inicio de una palabra
    split = (char **)malloc(sizeof(char *) * (ft_count_words(str) + 1));        // Reservo memoria en función del número de palabras
    if (!split)                                                                 // Protego el malloc
        return (NULL);
    while (str[i] != '\0')                                                      // Recorro el argumento
    {
        while ((str[i] != '\0')                                                 // Recorro el argumento mientras el carácter sea de tipo espacio y aumento el contador
            && (ft_type_char(str[i]) == 0))
            i++;
        init_word = i;                                                          // asigno el inicio de una palabra al contador
        while ((str[i] != '\0')                                                 // Recorro el argumento mientras el carácter sea printable y aumento el contador
            && (ft_type_char(str[i]) == 1))
            i++;
        if (init_word != i)                                                     // Si he vanzado de posición (init_word e i no son iguales)
        {
            split[j] = (char *)malloc(sizeof(char) * ((i - init_word) + 1));    // Reservo memoria en función del número de carácteres de la palabra
            ft_strncpy(split[j++], &str[init_word], (i - init_word));           // Copio los carácteres entre init_word e i con ft_strncpy en el array split y aumento el contador de este array
        }
    }
    split[j] = '\0';                                                            // Cierro en la última posición
    return (split);
}

/*SANDRA BUENA*/
#include <stdlib.h>

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
/*
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
}
*/

/*
int main(void)
{
    char **split;

    split = ft_split("Cada palabra una linea");
	printf("Cada    --> %s\n", split[0]);
    printf("palabra --> %s\n", split[1]);
    printf("una     --> %s\n", split[2]);
    printf("linea   --> %s\n", split[3]);
    return (0);
}
*/

/*
Assignment name  : ft_split
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
char **ft_split(char *str);
*/