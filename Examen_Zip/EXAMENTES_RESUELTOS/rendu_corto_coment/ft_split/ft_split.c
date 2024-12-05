/*Assignment name  : ft_split
Expected files   : ft_split.c
Allowed functions: malloc
--------------------------------------------------------------------------------
Write a function that takes a string, splits it into words, and returns them as
a NULL-terminated array of strings.
A "word" is defined as a part of a string delimited either by spaces/tabs/new
lines, or by the start/end of the string.
Your function must be declared as follows:
#include <unistd.h>;
--------------------------------------------------------------------------------
Escribe una función que tome una cadena, la divida en palabras y las devuelva como
una matriz de cadenas terminada en NULL.
Una "palabra" se define como parte de una cadena delimitada por espacios/tabulaciones/nueva
líneas, o por el inicio/final de la cadena.
Su función debe declararse de la siguiente manera:
char **ft_split(char *str);*/

/* FUNCIONA Y PASA MAQUINA IÑAKI */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// Definición de ft_strncpy- SACAR DE MAN Y AJUSTAR PONER FT_ =0 Y BAJAR I++
char *ft_strncpy(char *dest, const char *src, size_t n)
{
    size_t i = 0;

    // Copiar caracteres de src a dest hasta n caracteres o hasta que src termine
    while (i < n && src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
   // Si quedan caracteres en dest, rellenarlos con '\0'
    while (i < n)
    {
        dest[i] = '\0';
        i++;
    }
    // Retornar el puntero al destino
    return (dest);
}

// Función para verificar si un carácter es un espacio, tabulación o nueva línea
int ft_is_space(char c)
{
    return (c == 32 || c == 9 || c == 10);
}

// Función principal para dividir la cadena en palabras
char **ft_split(char *str)
{
    // Definir variables e inicialización de variables
	int i = 0;
    int j = 0;
    int words = 0;
    int k = 0;

    // Primer bucle para contar el número de palabras
    while (str[i])
    {
        // Saltar espacios en blanco
        while (str[i] && ft_is_space(str[i]))
            i++;
        // Si hay una palabra, incrementar el contador
        if (str[i])
            words++;
        // Avanzar hasta el final de la palabra
        while (str[i] && !ft_is_space(str[i]))
            i++;
    }
    // Reservar memoria para el array de punteros de cadenas
    char **out = (char **)malloc(sizeof(char *) * (words + 1));
    if (!out)
        return (NULL);  // Retorna NULL si no hay suficiente memoria

    // Reiniciar el índice para el segundo recorrido
    i = 0;
    while (str[i])
    {
        // Saltar espacios en blanco
        while (str[i] && ft_is_space(str[i]))
            i++;
        // Marcar el inicio de la palabra
        j = i;
        // Avanzar hasta el final de la palabra
        while (str[i] && !ft_is_space(str[i]))
            i++;
        // Si se ha encontrado una palabra (i > j)
        if (i > j)
        {
            // Reservar memoria para la palabra encontrada
            out[k] = (char *)malloc(sizeof(char) * (i - j + 1));
            if (!out[k])
				return (NULL);  // Verifica si la memoria fue asignada correctamente
            
			// Copiar la palabra al array de salida usando ft_strncpy
            ft_strncpy(out[k], &str[j], i - j);
            out[k][i - j] = '\0';  // Agregar el terminador nulo al final de la cadena copiada
            k++;
        }
    }
    out[k] = NULL;  // Marcar el final del array con NULL
    return (out);
}

int main(void)
{
    char **result;
    char str[] = "Hola esto es un test";
    int i = 0;

    result = ft_split(str);
    /*if (!result)
    {
        printf("Fallo alojamiento de memoria\n");
        return 1;
    } */

    while (result[i])
    {
        printf("%s\n", result[i]);
        i++;
    }
/*  free(result); */
    return (0);
}

int main(void)
{
    char **result;

    // Caso 1: Cadena muy larga
    char long_string[10000];
    int i = 0;
    while (i < 9999)
    {
        long_string[i] = 'a';
        i++;
    }
    long_string[9999] = '\0';
    result = ft_split(long_string);
    printf("Case 1: Very long string\n");
    if (result[0])
        printf("First word: %s\n", result[0]);
    else
        printf("No words found\n");

    // Caso 2: Solo espacios/tabulaciones
    char spaces_only[] = " \t\t  \t";
    result = ft_split(spaces_only);
    printf("Case 2: Spaces only\n");
    if (result[0])
        printf("First word: %s\n", result[0]);
    else
        printf("No words found\n");

    // Caso 3: Muchas palabras
    char many_words[] = "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10";
    result = ft_split(many_words);
    printf("Case 3: Many words\n");
    if (result[0])
        printf("First word: %s\n", result[0]);
    if (result[1])
        printf("Second word: %s\n", result[1]);
    if (result[2])
        printf("Third word: %s\n", result[2]);
    if (result[3])
        printf("Fourth word: %s\n", result[3]);
    if (result[4])
        printf("Fifth word: %s\n", result[4]);

    // Caso 4: Palabras largas
    char long_words[] = "ThisIsAVeryLongWordThatMightBeTooLongForTheBuffer ButThisOneIsShort";
    result = ft_split(long_words);
    printf("Case 4: Long words\n");
    if (result[0])
        printf("First word: %s\n", result[0]);
    if (result[1])
        printf("Second word: %s\n", result[1]);

    // Caso 5: Caracteres especiales y espacios múltiples
    char special_chars[] = "Hello,   World!   This is a test.";
    result = ft_split(special_chars);
    printf("Case 5: Special characters and multiple spaces\n");
    if (result[0])
        printf("First word: %s\n", result[0]);
    if (result[1])
        printf("Second word: %s\n", result[1]);
    if (result[2])
        printf("Third word: %s\n", result[2]);
    if (result[3])
        printf("Fourth word: %s\n", result[3]);
    if (result[4])
        printf("Fifth word: %s\n", result[4]);

    return (0);
}


/* FUNCIONA PERO NO PASA MAQUINA IÑAKI */
/* #include <stdio.h>

int es_espacio(char c)
{
    return (c == 32 || (c >= 9 && c <= 13));
}

char **ft_split(char *str)
{
    static char words_array[1024][4096];
    static char *words[1025]; // 1024 + 1z
    int i = 0, j = 0, k = 0;

    while (str[i])
    {
        while (str[i] && es_espacio(str[i]))
            i++;
        if (!str[i])
            break;
        k = 0;
        while (str[i] && !es_espacio(str[i]) && k < 4095) // 4096 - 1
        {
            words_array[j][k] = str[i];
            k++;
            i++;
        }
        words_array[j][k] = '\0';
        words[j] = words_array[j];
        j++;

        if (j >= 1024)
            break;
    }
    words[j] = NULL;
    return (words);
} */

