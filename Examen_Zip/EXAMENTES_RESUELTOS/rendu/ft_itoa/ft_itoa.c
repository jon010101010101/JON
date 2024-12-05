#include <stdlib.h>

int nlen(long nbr)
{
    int n = 0;
    if (nbr <= 0)
        n++;
    while (nbr != 0)
    {
        n++;
        nbr = nbr / 10;
    }
    return (n);
}

char *ft_itoa(int nbr)
{
    long num = nbr;
    int len = nlen(num);
    char *str = (char *)malloc(sizeof(char) * (len + 1));
    if (!str)
        return (NULL);
    
    str[len] = '\0';
    if (num < 0)
    {
        str[0] = '-';
        num = -num;
    }
    if (num == 0)
    {
        str[0] = '0';
    }
    while (num != 0)
    {
        str[--len] = (num % 10) + '0';
        num = num / 10;
    }
    return (str);
}
