#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char * ft_strncpy(char *dest, const char *src, size_t n)
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
    return (c == ' ' || c == '\t' || c == '\n');
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

/* int main(void)
{
    char **frase = ft_split("a ver si apruebo de una vez");
    int i = 0;

    while (frase[i])
    {
        printf("%d: %s\n", i, frase[i]);
        free(frase[i]);
        i++;
    }
    free(frase);
    return (0);
} */