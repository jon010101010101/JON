/*Escribe una función que tome una cadena, la divida en palabras y las devuelva como
una matriz de cadenas terminada en NULL.
Una "palabra" se define como parte de una cadena delimitada por espacios/tabulaciones/nueva
líneas, o por el inicio/final de la cadena.
Su función debe declararse de la siguiente manera:
char **ft_split(char *str);
*/
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char *ft_strncopy(char *s1, char *s2, int n)
{
	int i;

	i = 0;
	while (s2[i] && i < n)
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] ='\0';
	return (s1);
}
int ft_is_space(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

char **ft_split(char *str)
{
	int i;
	int j;
	int k;
	char **out;
	int words;
	
	i = 0;
	j = 0;
	k = 0;
	words = 0;
	while (str[i])
	{ 
		while (str[i] && ft_is_space(str[i]))
			i++;
		if (str[i])
			words ++;
		while (str[i] && !ft_is_space(str[i]))
			i++;		
	}
	out = (char **)malloc(sizeof(char *) * (words +1));
	if (!out)
		return(NULL);
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
			out[k]	= (char *)malloc(sizeof(char) * (i -j + 1));
			ft_strncopy(out[k++], &str[j], i-j);
		}
	}	
	out[k] = NULL;
	return (out);
}

/*int main (void)
{
	char **frase = ft_split("     la verdad tengo ganas de acabar    ");
	int i = 0;
	while (frase[i])
	{
		printf("%d : %s\n", i, frase[i]);
		i++;
	}
	return (0);
}*/

/*#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int ft_is_space (char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

char	*ft_strn_copy(char *str1, char*str2, int n)
{
	int i;

	i = 0;
	while (str2[i] && i < n)
	{
		str1[i] = str2[i];
		i++;
	}
	str1[i] = '\0';
	return (str1);
}

char **ft_split(char *str)
{
	int i;
	int j;
	int k;
	int words;

	i = 0;
	j = 0;
	k = 0;
	words = 0;

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
			out[k] =  (char *)malloc(sizeof(char) * (i - j +1));
			ft_strn_copy(out[k++], &str[j], i-j);
		}
	}
	out[k] = NULL;
	return (out);
}

int main (void)
{
	char **frase = ft_split("     la verdad tengo ganas de acabar    ");
	int i = 0;
	while (frase[i])
	{
		printf("%d : %s\n", i, frase[i]);
		i++;
	}
	return (0);
}*/
