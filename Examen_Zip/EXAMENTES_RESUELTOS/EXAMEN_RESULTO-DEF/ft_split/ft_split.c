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

/* ES OK Y PASA MAQUINA */

/* #include <unistd.h>
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
    return (c == ' ' || c == '\t' || c == '\n');
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
    // Dividir la cadena de ejemplo en palabras
    char **frase = ft_split("a ver si apruebo de una vez");
    int i = 0;
    // Imprimir cada palabra resultante
    while (frase[i])
    {
        printf("%d: %s\n", i, frase[i]);
        free(frase[i]);  // Liberar la memoria de cada palabra
        i++;
    }
    free(frase);  // Liberar la memoria del array de punteros
    return (0);
} */


/* ANA PASA MAQUINA*/

/* #include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char	*ft_strcopy(char *str1, char *str2, int n)
{
	int	i;
	
	i = 0;
	while (i < n && str2[i])
	{
		str1[i] =str2[i];
		i++;
	}
	str1[i] = '\0';
	return (str1);
}

int ft_is_space(char c)
{
	return( c == ' ' || c == '\t' || c == '\n');
}

char    **ft_split(char *str)
{
	int i;
	int j;
	int words;
	int k;

	i = 0;
	j = 0;
	words = 0;
	k = 0;
	
	
	while (str[i])
	{
		while (str[i] && ft_is_space(str[i]))
		{
			i++;
		}
		if (str[i])
		{
			words++;
		}
		while (str[i] && !ft_is_space(str[i]))
		{
			i++;
		}
	}
	char **out = (char **)malloc(sizeof(char *) * (words + 1));
	if (!out)
	{
		return (NULL);
	}
	i = 0;
	while (str[i])
	{
		while (str[i] && ft_is_space(str[i]))
		{
			i++;
		}
		j = i;
		while (str[i] && !ft_is_space(str[i]))
		{
			i++;
		}
		if (i > j)
		{
			out[k] = (char *)malloc(sizeof(char) * (i - j + 1));
			ft_strcopy(out[k++], &str[j], i-j);
		}
	}
	out[k] = NULL;
	return (out);
} */
/* 
int main (void)
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
  
/* COMENTARIOS ANA */

/* #include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// Función para copiar `n` caracteres de `str2` a `str1`
// y añadir un terminador nulo al final
char	*ft_strcopy(char *str1, char *str2, int n)
{
	int	i;
	
	i = 0;
	// Copiar cada carácter de str2 a str1 hasta un máximo de n caracteres
	while (i < n && str2[i])
	{
		str1[i] = str2[i];
		i++;
	}
	// Agregar el terminador nulo al final de str1
	str1[i] = '\0';
	return (str1);
}

// Función para verificar si un carácter es un espacio, tabulación o nueva línea
int ft_is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

// Función principal para dividir la cadena en palabras
char **ft_split(char *str)
{
	int i;      // Índice para recorrer la cadena original
	int j;      // Índice para marcar el inicio de una palabra
	int words;  // Contador de palabras encontradas
	int k;      // Índice para recorrer el array de palabras

	// Inicializar los índices y el contador de palabras
	i = 0;
	j = 0;
	words = 0;
	k = 0;
	
	// Primer bucle para contar el número de palabras en la cadena original
	while (str[i])
	{
		// Saltar todos los espacios en blanco
		while (str[i] && ft_is_space(str[i]))
		{
			i++;
		}
		// Si hay una palabra, incrementar el contador de palabras
		if (str[i])
		{
			words++;
		}
		// Saltar todos los caracteres de la palabra actual
		while (str[i] && !ft_is_space(str[i]))
		{
			i++;
		}
	}

	// Reservar memoria para un array de punteros de cadenas (cantidad de palabras + 1 para el NULL final)
	char **out = (char **)malloc(sizeof(char *) * (words + 1));
	if (!out)
	{
		return (NULL); // Si falla la asignación de memoria, retorna NULL
	}

	// Restablecer el índice para recorrer la cadena nuevamente
	i = 0;
	// Bucle principal para extraer cada palabra de la cadena original
	while (str[i])
	{
		// Saltar todos los espacios en blanco
		while (str[i] && ft_is_space(str[i]))
		{
			i++;
		}
		// Marcar el inicio de la palabra
		j = i;
		// Continuar hasta encontrar el final de la palabra
		while (str[i] && !ft_is_space(str[i]))
		{
			i++;
		}
		// Si se encontró una palabra (es decir, i > j)
		if (i > j)
		{
			// Asignar memoria para la palabra encontrada
			out[k] = (char *)malloc(sizeof(char) * (i - j + 1));
			// Copiar la palabra al array de salida
			ft_strcopy(out[k++], &str[j], i - j);
		}
	}
	// Marcar el final del array con NULL
	out[k] = NULL;
	return (out);
}

// Función principal para probar la función ft_split
int main(void)
{
	// Dividir la cadena de ejemplo en palabras
	char **frase = ft_split("a ver si apruebo de una vez");
	int i = 0;
	// Imprimir cada palabra resultante
	while (frase[i])
	{
		printf("%d: %s\n", i, frase[i]);
		i++;
	}
	return (0);
} */


/* FUNCIONA PERO NO PASA MAQUINA */
/* #include <stdio.h>

// Función para verificar si un carácter es un espacio en blanco
int es_espacio(char c)
{
    return (c == 32 || (c >= 9 && c <= 13));
}

char **ft_split(char *str)
{
    static char words_array[1024][4096];
    static char *words[1025]; // 1024 + 1
    int i = 0, j = 0, k = 0;

    while (str[i])
    {
        // Ignorar caracteres de espacio en blanco
        while (str[i] && es_espacio(str[i]))
            i++;
        if (!str[i])
            break;
        k = 0;
        // Copiar caracteres hasta el siguiente espacio en blanco
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

int main()
{
    char str[4096] = "Hola, esta es una prueba\ncon\tvarias palabras.";
    char **words = ft_split(str);
    int i = 0;

    while (words[i])
    {
        printf("Palabra %d: %s\n", i, words[i]);
        i++;
    }
    return (0);
} */