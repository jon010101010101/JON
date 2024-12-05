#include <unistd.h>
#include <stdlib.h>

int ft_count(int nbr)
{
    int count = (nbr <= 0);

    while(nbr)
    {
        nbr = nbr / 10;
        count++;
    }
    return(count);
}

char *ft_itoa(int nbr)
{
    char *digits;
    char *newstr;
    int len;
    long num;

    num = nbr;
    len = ft_count(nbr);
    digits = "0123456789";
    newstr=(char *)malloc(sizeof(char) * (len + 1));
    if(!newstr)
        return(NULL);
    newstr[len]='\0';
    len = len - 1;
    if(num == 0)
        newstr[0]='0';
    if(num < 0)
    {
        newstr[0]='-';
        num = - num;
    }
    while(num != 0)
    {
        newstr[len]=digits[ num % 10];
        num = num / 10;
        len--;
    }
    return(newstr);
}

/* #include <stdio.h>
#include <limits.h>

int main(void)
{
    char *str;

    str=ft_itoa(INT_MIN);
    printf("%s\n", str);
    free(str);

    str=ft_itoa(INT_MAX);
    printf("%s\n", str);
    free(str);

    str=ft_itoa(0);
    printf("%s\n", str);
    free(str);

    

    return(0);
} */