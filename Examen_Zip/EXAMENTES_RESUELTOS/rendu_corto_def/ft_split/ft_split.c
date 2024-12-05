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

/* FUNCIONA Y PASA MAQUINA */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// Definición de ft_strncpy- SACAR DE MAN Y AJUSTAR PONER FT_ =0 Y BAJAR I++, 
// QUITAR LAS CERO
char *ft_strncpy(char *dest, const char *src, size_t n)
{
    size_t i = 0;

    while (i < n && src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
    while (i < n)
    {
        dest[i] = '\0';
        i++;
    }
    return (dest);
}

int ft_is_space(char c)
{
    return (c == 32 || c == 9 || c == 10);
}

char **ft_split(char *str)
{
	int i = 0;
    int j = 0;
    int words = 0;
    int k = 0;

    while (str[i])
    {
        while (str[i] && ft_is_space(str[i]))
            i++;
        if (str[i])
            words++;
        while (str[i] && !ft_is_space(str[i]))
            i++;
    }
    char **out = (char **)malloc(sizeof(char *) * (words + 1));
    if (!out)
        return (NULL);
    i = 0;
    while (str[i])
    {
        while (str[i] && ft_is_space(str[i]))
            i++;
        j = i;
        while (str[i] && !ft_is_space(str[i]))
            i++;
        if (i > j)
        {
            out[k] = (char *)malloc(sizeof(char) * (i - j + 1));
            if (!out[k])
				return (NULL);
            ft_strncpy(out[k], &str[j], i - j);
            out[k][i - j] = '\0';
            k++;
        }
    }
    out[k] = NULL;
    return (out);
}

/* MAIN CORTO, FUNCIONA SIN LO COMENTADO PARA SIMPLIFICAR, CONVIENE COMPLETO,
PARA TENER POSIBLE FALLO MEMORIA Y LIBERACION MALLOC*/

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


/* CON VARIAS PRUEBAS A LA VEZ */

 int main(void)
{
    char **result;

    // Caso 1: Cadena muy larga
    char string[4000];
    int i = 0;
    while (i < 3999)
    {
        string[i] = 'a';
        i++;
    }
    string[9999] = '\0';
    result = ft_split(string);
    printf("Caso 1: Cadena muy larga\n");
    if (result[0])
        printf("Primera palabra: %s\n", result[0]);
    else
        printf("No se han encontrado palabras\n");
    printf("\n");

    // Caso 2: Solo espacios/tabulaciones
    char spaces_only[] = " \t\t  \t";
    result = ft_split(spaces_only);
    printf("Caso 2: Solo espacios/tabulaciones\n");
    if (result[0])
        printf("Primera palabra: %s\n", result[0]);
    else
        printf("No se han encontrado palabras\n");
    printf("\n");

    // Caso 3: Muchas palabras
    char many_words[] = "Palabra1 Palabra2 Palabra3 Palabra4 Palabra5 Palabra6 Palabra7";
    result = ft_split(many_words);
    printf("Caso 3: Muchas palabras\n");
    if (result[0])
        printf("Primera palabra: %s\n", result[0]);
    if (result[1])
        printf("Segunda palabra: %s\n", result[1]);
    if (result[2])
        printf("Tercera palabra: %s\n", result[2]);
    if (result[3])
        printf("Cuarta palabra: %s\n", result[3]);
    if (result[4])
        printf("Quinta palabra: %s\n", result[4]);
    if (result[5])
        printf("Sexta palabra: %s\n", result[5]);
    if (result[6])
        printf("Séptima palabra: %s\n", result[6]);
    printf("\n");
    
    // Caso 4: Palabras largas
    char long_words[] = "Estaesunapalabramuylargaquepodríaserdemasiadolargaparaelbúfer, peroéstaescorta";
    result = ft_split(long_words);
    printf("Caso 4: Palabras largas\n");
    if (result[0])
        printf("Primera palabra: %s\n", result[0]);
    if (result[1])
        printf("Segunda palabra: %s\n", result[1]);
    printf("\n");

    // Caso 5: Caracteres especiales y espacios múltiples
    char special_chars[] = "Hola,   Gente!   Esto es un test.";;
    result = ft_split(special_chars);
    printf("Caso 5: Caracteres especiales y espacios múltiples\n");
    if (result[0])
        printf("Primera palabra: %s\n", result[0]);
    if (result[1])
        printf("Segunda palabra: %s\n", result[1]);
    if (result[2])
        printf("Tercera palabra: %s\n", result[2]);
    if (result[3])
        printf("Cuarta palabra: %s\n", result[3]);
    if (result[4])
        printf("Quinta palabra: %s\n", result[4]);
    if (result[5])
        printf("Sexta palabra: %s\n", result[5]);
    printf("\n");

    // 6. Caso: Cadena vacía
    char empty_string[] = "";
    result = ft_split(empty_string);
    printf("Caso 6: Cadena vacía\n");
    if (result && result[0] == NULL)
        printf("La cadena esta vacía\n");
    else
        printf("No se han encontrado palabras\n");
    printf("\n");
    
    if (result == NULL)
        printf("No se han encontrado palabras\n");

    return (0);
}


/* FUNCIONA PERO NO PASA MAQUINA */
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
}

/* int main (void)
{
	char **frase = ft_split("a ver si apruebo de una vez");
	int i = 0;
	while (frase[i])
	{
		printf("%d: %s\n", i, frase[i]);
		i++;
	}
	return (0);
} */

